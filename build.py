import codecs, cv, datetime
from jinja2 import Environment, FileSystemLoader
env = Environment(
    block_start_string = '%{',
    block_end_string = '%}',
    variable_start_string = '%{{',
    variable_end_string = '%}}',
    comment_start_string = '%{#',
    comment_end_string = '%#}',
    line_comment_prefix = '%#',
    line_statement_prefix = '%##',
    loader = FileSystemLoader('templates/')
)

""" Return the formatted date """
def format_date():
    return datetime.date.today().strftime("%m/%d/%Y")

def resume(outfile):
    template = env.get_template('resume.tex.jinja')
    with codecs.open(outfile, "wb", encoding="utf-8") as f:
            f.write(template.render(
                last_updated = format_date(),
                git_hash = cv.get_git_hash(),
                objective = None,
                schools = cv.get_schools(),
                experience = cv.get_experience(),
                skills = cv.get_skills(),
                languages = cv.get_languages(),
                interests = cv.get_interests()
            ))

if __name__=="__main__":
    outfile = 'output/resume.tex'
    resume(outfile)
