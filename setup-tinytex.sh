#!/usr/bin/env bash
#
# Setup TinyTeX
#
# https://yihui.org/tinytex/
#

# Install TinyTeX
curl -sL "https://yihui.org/tinytex/install-bin-unix.sh" | sh
# Install common LaTeX packages
tlmgr install \
	anyfontsize \
	ctex \
	datetime \
	enumitem \
	etaremune \
	everysel \
	fancyhdr \
	fmtcount \
	geometry \
	hyperref \
	sourcesanspro \
	sourcecodepro \
	xcolor
