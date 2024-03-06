cd examples
find ./ -name "*.md" \
    -type f \
    -exec sh -c \
    'kramdoc --format=GFM \
        --wrap=ventilate \
        --output={}.adoc {}' \;

cd ..