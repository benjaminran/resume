#!/usr/bin/env python3
import codecs
import datetime
import os
from jinja2 import Environment, FileSystemLoader
from .content import Content


def format_date():
    return datetime.date.today().strftime("%m/%d/%Y")


def jinjaEnvironment(template):
    template_dir, template_file = os.path.split(template)
    return Environment(
        block_start_string='%{',
        block_end_string='%}',
        variable_start_string='%{{',
        variable_end_string='%}}',
        comment_start_string='%{#',
        comment_end_string='%#}',
        line_comment_prefix='%#',
        line_statement_prefix='%##',
        loader=FileSystemLoader(template_dir)
    ) if template_file.endswith('.tex.jinja') else Environment(
        loader=FileSystemLoader(template_dir)
    )


def build(outfile, template, content_file):
    content = Content(content_file)
    template_dir, template_file = os.path.split(template)
    output_dir, output_file = os.path.split(outfile)
    env = jinjaEnvironment(template)
    template = env.get_template(template_file)
    with codecs.open(outfile, "wb", encoding="utf-8") as f:
        f.write(template.render(
            last_updated=format_date(),
            git_hash=content.get_git_hash(),
            schools=content.get_schools(),
            experience=content.get_experience(),
            skills=content.get_skills(),
            languages=content.get_languages(),
        ))
    if template_file.endswith('.tex.jinja'):
        os.system('lualatex -shell-escape --output-directory="'
                  + output_dir + '" ' + outfile)
