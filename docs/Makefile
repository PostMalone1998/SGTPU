# You can set these variables from the command line.

# module_name === project in conf.py, use \_ instead of _ if module name contains _
module_name := SGTPU
output_file_prefix := SGTPU软件指南

SOURCEDIR_zh    = source
pdf_name_zh      = $(output_file_prefix).pdf

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
BUILDDIR_zh      = build


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR_zh)" "$(BUILDDIR_zh)" $(SPHINXOPTS) $(O)

pdf: latex
	@cd $(BUILDDIR_zh)/latex && xelatex $(module_name).tex
	@cd $(BUILDDIR_zh)/latex && xelatex $(module_name).tex
	@mv $(BUILDDIR_zh)/latex/$(module_name).pdf $(BUILDDIR_zh)/"${pdf_name_zh}" && rm -rf $(BUILDDIR_zh)/latex

# web: html
# 	#@python3 -m http.server --directory build/html

clean:
	@rm -rf $(BUILDDIR_zh)
