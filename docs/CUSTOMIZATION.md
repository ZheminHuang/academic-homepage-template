# Customization

## Identity and Links

Edit the name, role, department, university, email, and external profile URLs in
`index.html` and `cv/index.html`. The default Scholar/GitHub/LinkedIn URLs lead to
the services' homepages, not to a personal account. Replace the profile links
with your own destinations. The mail address uses the reserved `example.com` domain.

Update the page title, description, Open Graph title/description, image alt text,
and footer too. Add absolute canonical, `og:url`, and `og:image` metadata only once
you know your final public URL. The starter deliberately does not hard-code a
domain, sitemap, university logo, or tracking service.

## Portrait

Replace the image `src`, `alt`, `width`, and `height` in `.portrait`. Use the real
intrinsic image dimensions for the attributes. The visible frame remains 4:5.
The default crop is centered in both directions, with no extra zoom.

Set `--portrait-scale` in `styles.css` to a value such as `1.1` for a closer crop.
Set it back to `1` to remove the extra zoom. The monogram is an original placeholder,
not a generated or stock photograph.

## Appearance

The first `:root` block in `styles.css` contains theme tokens:

```css
--accent: #8553a4;
--link: #326879;
--frame-radius: 18px;
--portrait-scale: 1;
```

The layout uses three columns at 1160px and wider, two columns at 800-1159px,
and one column below 800px. About Me and Research share `.overview`. Publications,
News, and Reviewer Service each have their own frame; individual paper rows do not.

After changing the shared stylesheet, increment `?v=1` in the two HTML files if
you need to bypass old browser caches.

## News

Duplicate a `.news-list > li`, update the text and machine-readable `datetime`,
and keep the newest item first. Use `YYYY-MM` for month-level dates. Move the
`news-badge` to the newest item; do not repeat it on every item. All news is visible
without an expansion control.

## Papers and Downloads

Duplicate a `.publication` article in `index.html`. Update the title, authors,
venue, date, summary, image dimensions, image `alt`, and each resource link.
Update the corresponding citation in the CV separately.

Replace the diagrams with your own paper figures. The `.publication-image--figure`
class uses `object-fit: contain` and preserves the complete figure. Set the enclosing
anchor's `href` to the same file so readers can inspect the full-resolution image.

Put permitted PDF versions in a new `assets/papers/` folder. Add only the links
that exist for your paper inside `.publication-links`, for example:

```html
<a href="assets/papers/2026-my-paper.pdf" download>PDF</a>
<a href="assets/bib/2026-my-paper.bib" download>BibTeX</a>
```

For DOI or project links, supply the real full URL. Never leave an `href="#"`
placeholder in a published row. No PDF is bundled with this template; the example
BibTeX files are clearly marked as fictional and include publication months.
For your real citations, verify the published author order, venue abbreviation,
volume/issue, page range or article number, month/year, and DOI.

## Reviewer Service and CV

Each review record is a list item. Use the full venue name, abbreviation, and
year(s). Keep the homepage and CV lists consistent. You can print the CV from
the browser; the print stylesheet removes the home link and unnecessary decoration.

## Optional Pointer Effect

Remove the `assets/js/click-effects.js` script element in the homepage and the
`../assets/js/click-effects.js` script element in the CV to disable it. To customize
the symbols, edit the `symbols` array. The effect already respects reduced-motion
preferences and never blocks links. All page content works with JavaScript disabled.

## Deployment and Checks

Use **Settings > Pages > Deploy from a branch > main > /(root)**. Keep `.nojekyll`.
For official setup details, see the
[GitHub Pages publishing guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

To enable the **Use this template** button on your own reusable repository, its
owner can select **Settings > General > Template repository**. See
[GitHub's template documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository).

If assets disappear on a project site, check for accidental root-relative paths
such as `/styles.css`. The homepage should use `styles.css`; the CV should use
`../styles.css`. Run `python3 scripts/check.py` to catch these mistakes and missing
local files. Always preview at 320px and a desktop width after editing long text.

The repository intentionally omits a custom 404 page, legacy redirects, private
source files, unpublished manuscripts, and personal data from the original site.
It is a clean, independent starting point, not a copy of the author's Git history.
