#!/usr/bin/env python
import subprocess
import xml.etree.ElementTree as ET
cv = ET.parse('cv.xml').getroot()

""" Return the current git coordinates """
def get_git_hash():
    return subprocess.Popen(["util/git-coordinates.sh", ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode("utf-8").strip()

def get_schools():
    return [{
        'name': school.find('./name').text,
        'location': school.find('./location').text,
        'timespan': school.find('./timespan').text,
        'major': school.find('./major').text if school.find('./major') is not None else None,
        'coursework': [course.attrib['name'] for course in school.findall('./coursework/course')],
        'gpa': school.find('./gpa').text
    } for school in cv.findall('./education/school')]

def expand_links2(links):
    return " | ".join([str.format("\\href{{{0}}}{{{1}}}", link.attrib['url'], link.attrib['title']) for link in links.findall("./link")])

def expand_description2(desc):
    output = desc.find("./general").text
    if output is None: output=""
    if len(desc.findall("./details/detail"))!=0: output+="\n\\begin{itemize*}\n" + "".join(["  \\item "+detail.text.strip()+"\n" for detail in desc.findall("./details/detail")]) + "\\end{itemize*}\n"
    return output

def expand_links(exp):
    return [link.attrib for link in exp.findall('./links/link')]

def expand_description(exp):
    return {'general': exp.find('./description/general').text,
            'details': [detail.text.strip() for detail in exp.findall('./description/details/detail')]}

def get_experience():
    return [
        {
            'title': exp.find('./employer').text,
            'location': exp.find('./location').text,
            'timespan': exp.find('./timespan').text,
            'subtitle': exp.find('./position').text,
            'links': expand_links(exp),
            'description': expand_description(exp)
        } if exp.attrib['type']=='work' else
        {
            'title': exp.find('./hackathon').text,
            'timespan': exp.find('./timespan').text,
            'subtitle': 'Developer',
            'links': expand_links(exp),
            'description': expand_description(exp)
        } if exp.attrib['type']=='hackathon' else
        {
            'title': exp.find('./name').text,
            'timespan': exp.find('./timespan').text,
            'subtitle': 'Private Project',
            'links': expand_links(exp),
            'description': expand_description(exp)
        }
        for exp in cv.findall("./experience/exp[category='include']")]

def get_experience2():
    for exp in cv.findall("./experience/exp[category='include']"):
        if exp.attrib['type']=='work':
            print(str.format("\\textbf{{{0}}}, {1} \\rdate{{{2}}}\\\\\n\\emph{{{3}}} \\hfill \\suplinks{{{4}}}\\\\\n{5}\\medskip\n",
                             exp.find("./employer").text,
                             exp.find("./location").text,
                             exp.find("./timespan").text,
                             exp.find("./position").text,
                             expand_links(exp.find("./links")),
                             expand_description(exp.find("./description"))))
        elif exp.attrib['type']=='hackathon':
            print(str.format("\\textbf{{{0}}} \\rdate{{{1}}}\\\\\n\\emph{{{2}}} \\hfill \\suplinks{{{3}}}\\\\\n{4}\\medskip\n",
                             exp.find("./hackathon").text,
                             exp.find("./timespan").text,
                             "Developer",
                             expand_links(exp.find("./links")),
                             expand_description(exp.find("./description"))))
        elif exp.attrib['type']=='private project':
           print(str.format("\\textbf{{{0}}} \\rdate{{{1}}}\\\\\n\\emph{{{2}}} \\hfill \\suplinks{{{3}}}\\\\\n{4}\\medskip\n",
                            exp.find("./name").text,
                            exp.find("./timespan").text,
                            "Private Project",
                            expand_links(exp.find("./links")),
                            expand_description(exp.find("./description"))))

def get_skills():
    return [skill.attrib['name'] for skill in cv.findall("./skills/skill")]
#return "\\begin{itemize}"+"".join(["\item "+skill.attrib['name']+"\n" for skill in cv.findall("./skills/skill")])+"\\end{itemize}"

def get_languages():
    return [language.text for language in cv.findall("./languages/language")]

def get_interests():
    return [interest.attrib['name'] for interest in cv.findall("./interests/interest")]

if __name__=="__main__":
    get_projects()




