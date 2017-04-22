#!/usr/bin/env python3
import codecs
import datetime
import argparse
import os
import re
from jinja2 import Environment, FileSystemLoader
from .content import Content

#
# Build final latex from sources
#


def format_date():
    return datetime.date.today().strftime("%m/%d/%Y")


def build(outfile, template, content_file):
    content = Content(content_file)
    template_dir, template_file = os.path.split(template)
    output_dir, output_file = os.path.split(outfile)
    env = Environment(
        block_start_string='%{',
        block_end_string='%}',
        variable_start_string='%{{',
        variable_end_string='%}}',
        comment_start_string='%{#',
        comment_end_string='%#}',
        line_comment_prefix='%#',
        line_statement_prefix='%##',
        loader=FileSystemLoader(template_dir)
    )
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
    os.system('lualatex -shell-escape --output-directory="'
              + output_dir + '" ' + outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template_dir', default='/resume/templates',
                        help='path to templates directory')
    parser.add_argument('-o', '--output_dir', help='path to output file',
                        default='/resume/output')
    parser.add_argument('-c', '--content', help='path to cv.xml',
                        default='/resume/content/cv.xml')
    args = parser.parse_args()
    for template in os.listdir(args.template_dir):
        build(
            os.path.abspath(
                os.path.join(
                    args.output_dir, re.sub('\.jinja$', '', template)
                )
            ),
            os.path.abspath(
                os.path.join(args.template_dir, template)
            ),
            os.path.abspath(args.content)
        )
