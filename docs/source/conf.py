# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'SGTPU'
copyright = u'2022, SOPHGO'
author = u'SOPHGO'

project_full_name = 'SGTPU软件指南'

import subprocess
command_line = "git describe --tags --always"
tag_str = u""
try:
    tag_str = subprocess.check_output(command_line, shell = True).decode()
except subprocess.TimeoutExpired as time_e:
    print(time_e)
except subprocess.CalledProcessError as call_e:
    print(call_e.output.decode(encoding="utf-8"))
release = tag_str.lstrip('v')

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'

latex_engine = 'xelatex'
latex_elements = {
    # Papersize ('letterpaper' or 'a4paper'), default is letterpaper
    'papersize': 'a4paper',
    # 设置页边距大小
    'geometry': r' \usepackage[left=2.8cm,right=2.6cm,top=3.7cm,bottom=3.5cm]{geometry}',
    # The font size ('10pt', '11pt' or '12pt'), default is '10pt'.
    'pointsize': '11pt',
    # \setCJKmainfont[BoldFont=Heiti SC Medium]{Heiti SC Light}
    # \setCJKmonofont[BoldFont=Times Regular]{Times Italic}
    # `\setmainfont`、`\setsansfont{}`、`\setmonofont{}`
    # 分别设置正文字体、无衬线字体: 标题、等宽字体: 用于抄录内容
    'fontpkg': r'''
    \setmainfont{FandolSong}
    \setsansfont{FandolHei}
    \setmonofont{FandolFang}
    ''',
    # 设置章节标题样式
    # \usepackage[Lenny]{fncychap}  Bjarne, Sonny, Lenny, Glenn, Conny, Rejne
    'fncychap': '\\usepackage[Sonny]{fncychap}',
    # 图片严格出现在文字处
    # 'figure_align': 'H',
    # preamble 样式
    # 目录样式: tocloft
    # 每节从新页面开始: newcommand{\sectionbreak}{\clearpage}
    # 全文文本左对齐: \usepackage[document]{ragged2e}
    'preamble':r'''
    \usepackage{tocloft}
    \renewcommand\cftfignumwidth{4em}
    \renewcommand\cfttabnumwidth{4em}
    \renewcommand\cftsecnumwidth{4em}
    \renewcommand\cftsubsecnumwidth{6em}
    \renewcommand\cftparanumwidth{6em}
    \usepackage{fancyhdr}
    \setlength\headheight{14pt}
    \fancypagestyle{normal}{
        \fancyhead[R]{}
        \fancyhead[C]{\leftmark}
        \fancyfoot[C]{Copyright © SOPHGO}
        \fancyfoot[R]{\thepage}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0pt}
    }
    ''',
    'extraclassoptions': 'openany,oneside',

    # 'classoptions': ',zh_CN',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

default_role = None

latex_documents = [
    (master_doc, project + '.tex', project_full_name, author, 'manual'),
]