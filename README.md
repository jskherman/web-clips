# Permanent Web Snapshots

This project is dedicated to the preservation of web content, ensuring its permanence for use in my Obsidian notes. It leverages the [SingleFile](https://chromewebstore.google.com/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle) web extension for saving webpages, Jekyll, a static site generator, for building the website, and bun/postcss/tailwind for styling.

This is forked from the [original project by Luke Chadwick](https://github.com/vertis/permanent-web-snapshots) with the main difference being the different files in the `snapshots` folder as well as the `_config.yml` file.

## Setup

To compile the CSS with Bun, do:

```bash
bun install
bun build-css
```

## Development

To run Jekyll locally, do:

```bash
bundle install
bundle exec jekyll serve -w
```
