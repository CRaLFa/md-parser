#!/bin/bash -x

readonly DATA_DIR='/tmp'
readonly BASE_DIR="$(dirname $0)"
readonly OUT_DIR="$BASE_DIR/output"

get_markdown () {
    find $DATA_DIR/ -name '*.md' | head -n 1
}

serve_error () {
    echo -e 'Content-Type: text/html\n'
    cat $BASE_DIR/template/error.html | sed "s/{}/$1/"
    exit 0
}

serve_html () {
    local md=$(get_markdown)
    [ -z "$md" ] && serve_error 'Please specify Markdown (.md) file.'
    echo -e 'Content-Type: text/html\n'
    pandoc -f gfm --template $BASE_DIR/template/template.html "$md"
}

serve_pdf () {
    local md=$(get_markdown)
    [ -z "$md" ] && serve_error 'Please specify Markdown (.md) file.'
    local pdf_name=$(basename ${md%.md}.pdf)
    pandoc -f gfm -t html5 "$md" -o $OUT_DIR/output.pdf || exit $?
    echo 'Content-Type: application/pdf'
    echo -e "Content-Disposition: inline; filename=\"$pdf_name\"\n"
    cat $OUT_DIR/output.pdf
}

if [[ "$QUERY_STRING" == *pdf* ]]; then
    serve_pdf
else
    serve_html
fi

exit 0
