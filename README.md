# Academic Homepage Template

A quiet, three-column academic homepage built with plain HTML and CSS.
Adapted from [Zhemin Huang's homepage](https://zheminhuang.github.io/), with
fictional content and reusable example graphics instead of personal materials.

[中文说明](README.zh-CN.md) · [Customization guide](docs/CUSTOMIZATION.md)

![Desktop preview of the example homepage](docs/preview-desktop.png)

<details>
<summary>Mobile preview</summary>

<img src="docs/preview-mobile.png" width="390" alt="Mobile preview of the example homepage">

</details>

## Included

- Profile sidebar with centered portrait framing and local link icons.
- About Me and Research in one rounded frame; Publications and Reviewer Service in separate matching frames.
- All-visible News with date badges, plus responsive tablet and mobile layouts.
- Uncropped paper thumbnails that link to full-size figures and downloadable BibTeX examples.
- A printable web CV, keyboard skip link, visible focus states, and reduced-motion support.
- Optional mathematical pointer effects. No analytics, remote fonts, framework, or build step.

All example people, affiliations, papers, venues, achievements, reviewing records,
and citations are fictional. The sample diagrams are illustrative, not research
results. Replace them before publishing your own academic record.

## Get Started

1. Use **Use this template** if enabled, or fork this repository.
2. Edit `index.html` and `cv/index.html` to replace the example identity and content.
3. Replace `assets/images/avatar.svg` and the example figures with your own images.
4. Enable GitHub Pages in **Settings > Pages**, using **Deploy from a branch**,
   branch **main**, folder **/(root)**.

Publishing settings are described in the
[official GitHub Pages guide](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
The included `.nojekyll` keeps this a plain static site.

Both deployment shapes are supported without changing asset paths:

- `https://USERNAME.github.io/` for a repository named `USERNAME.github.io`.
- `https://USERNAME.github.io/REPOSITORY/` for a project repository.

Links use document-relative paths. Keep them relative when adding new content;
do not change `assets/...` to `/assets/...` for a project site.

## Preview Locally

You can open `index.html` directly for a quick look. For consistent SVG icon
loading and download behavior, use a local HTTP server:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. If that port is in use, choose another port.
Python is only needed for the optional preview/check tools, not for hosting.

## Where to Edit

| Content | File |
| --- | --- |
| Name, biography, research, news, papers, reviewing | `index.html` |
| CV and its reviewing list | `cv/index.html` |
| Colors, corner radius, centered portrait zoom, breakpoints | `styles.css` |
| CV layout and print rules | `cv/cv.css` |
| Portrait and publication figures | `assets/images/` |
| Citation downloads | `assets/bib/` |
| Optional pointer effects | `assets/js/click-effects.js` |

The homepage and CV are independent HTML documents. Update shared information
in both places. See the [customization guide](docs/CUSTOMIZATION.md) for PDF
buttons, paper rows, profile links, metadata, and deployment troubleshooting.

## Check Your Changes

```bash
python3 scripts/check.py
```

The standard-library checker verifies local HTML links, image attributes,
fragment targets, SVG files, and relative paths. GitHub Actions runs the same
check on pushes and pull requests. It does not verify external website content.
Also inspect desktop and mobile layouts after changing text or images.

## License and Credits

The template code and original example graphics are available under the
[MIT License](LICENSE). Keep the license notice when redistributing the code;
the visible footer credit is appreciated but optional.

Lucide and Feather icons retain their licenses in
[`assets/icons/LICENSE.txt`](assets/icons/LICENSE.txt). See
[third-party notices](THIRD_PARTY_NOTICES.md) for sources and design references.
The original author's photo, university branding, actual publications, and PDF
files are **not included**. Check the rights to any images or PDFs you add.

## Contributing

Small, focused improvements are welcome. Please keep the site usable without
JavaScript or a build tool, run the checker, and include desktop/mobile screenshots
for visual changes. See [CONTRIBUTING.md](CONTRIBUTING.md).
