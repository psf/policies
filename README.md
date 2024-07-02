# Python Software Foundation Policies

This repository acts as the canonical source for the policies published by
the [Python Software Foundation](https://python.org/psf/).

## Development

You can use `docker compose up` to start development server with live-reloading as you
edit documents.

Once it has started, navigate to [http://localhost:10000](http://localhost:10000)
in your browser! Any edits made will render as you save your work.

### Adding new pages

To add a new page, you'll need to do two things:

1. Create the page itself in the appropriate location under [`./docs`](./docs/).
2. Add the page to the `nav` hierarchy in [`mkdocs.yml`](./mkdocs.yml).
