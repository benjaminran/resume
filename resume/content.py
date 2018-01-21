import pypandoc
import subprocess
import xml.etree.ElementTree as ET


class Content:
    def __init__(self, path):
        self.cv = ET.parse(path).getroot()

    def get_git_hash(self):
        return subprocess.check_output(
            ['git', 'log', '--abbrev-commit', '--pretty=oneline']
        ).decode('utf-8').split()[0]

    def get_schools(self):
        return [{
            'name': school.find('./name').text,
            'location': school.find('./location').text,
            'timespan': school.find('./timespan').text,
            'major': school.find('./major').text if school.find('./major') is not None else None,
            'coursework': [course.attrib['name'] for course in school.findall('./coursework/course')],
            'gpa': school.find('./gpa').text
        } for school in self.cv.findall('./education/school')]

    def expand_links(self, exp):
        return [link.attrib for link in exp.findall('./links/link')]

    def expand_description(self, exp):
        return {
            'general': pypandoc.convert_text(exp.find('./description/general').text, 'latex', format='md'),
            'details': [pypandoc.convert_text(detail.text.strip(), 'latex', format='md') for detail in exp.findall('./description/details/detail')]
        }

    def get_experience(self):
        return [
            {
                'title': exp.find('./employer').text,
                'location': exp.find('./location').text,
                'timespan': exp.find('./timespan').text,
                'subtitle': exp.find('./position').text,
                'links': self.expand_links(exp),
                'description': self.expand_description(exp)
            } if exp.attrib['type'] == 'work' else
            {
                'title': exp.find('./hackathon').text,
                'timespan': exp.find('./timespan').text,
                'subtitle': 'Developer',
                'links': self.expand_links(exp),
                'description': self.expand_description(exp)
            } if exp.attrib['type'] == 'hackathon' else
            {
                'title': exp.find('./name').text,
                'timespan': exp.find('./timespan').text,
                'subtitle': 'Private Project',
                'links': self.expand_links(exp),
                'description': self.expand_description(exp)
            }
            for exp in self.cv.findall("./experience/exp[category='include']")
        ]

    def get_skills(self):
        return [skill.attrib['name'] for skill in self.cv.findall("./skills/skill")]
