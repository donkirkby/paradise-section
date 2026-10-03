## Contributing

If you like the mazes and want to make them better, help out. It could be as
simple as sending [@donkirkby@hachyderm.io] a nice note on Mastodon, you could
report a problem, or pitch in with some test solving or design work.

### Problems

Found a typo or a problem? Create a [GitHub issue], and be as
specific as possible.

### New Puzzles

Do you have an idea for another puzzle to include? Create an issue, and describe
how it would work.

### Dev Tools

See installation details in `.github/workflows/python-app.yml`.

### Testing GitHub Pages locally

The website uses the [Bulma Clean theme], which is based on [Bulma]. The
[Bulma colours] can be particularly helpful to learn about.

The callouts use [Font Awesome icons], and you can search for many more free
icons there.

GitHub generates all the web pages from markdown files, but it can be useful to
test out that process before you commit changes. See the detailed instructions
for setting up [Jekyll], but the main command is this:

    bash -l
    rvm use 3.3.1
    cd docs
    bundle install
    bundler exec jekyll serve

[@donkirkby@hachyderm.io]: https://hachyderm.io/@donkirkby
[GitHub issue]: https://github.com/donkirkby/chess-kit/issues
[Bulma Clean theme]: https://github.com/chrisrhymes/bulma-clean-theme
[Bulma]: https://bulma.io/documentation/
[Bulma colours]: https://bulma.io/documentation/overview/colors/
[Font Awesome icons]: https://fontawesome.com/
[Jekyll]: https://help.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll
