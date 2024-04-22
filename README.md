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

## Notes

- Do not save webpages with titles that have special Unicode characters (e.g. `ᕕ( ᐛ )ᕗ`) because Jekyll will not be able to build the site.
  - If you do want to save a webpage with a title that has special Unicode characters, you will need to manually edit the HTML source first before you can save with the SingleFile web extension. The specifc HTML tag you will need to modify and remove non-ASCII characters is the `<title>` field under the `<head>` tag.
- In the SingleFile extension, if you decide to change the filename formatting of your HTML files, make sure to update the regex pattern for capturing the date in the `_plugins/extract_snapshot_metadata.rb` file.
