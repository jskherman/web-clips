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

- To myself:
  - Use Chrome to take advantage of the SingleFile extension's option to upload to Google Drive.
- Make sure that only ASCII characters are used in the filenames of the HTML files from the SingleFile extension.
- In the SingleFile extension, if you decide to change the filename formatting of your HTML files, make sure to update the regex pattern for capturing the date in the `_plugins/extract_snapshot_metadata.rb` file.
