# mimicing web page

## Things to Notate:

- **CSS-HTML Separation**: Separated the inline CSS from the HTML to create a more organized structure using external CSS (`mimic.css`).
  
- **Design Choices**: 
  - Used flexbox for the layout to create a simple two-column layout where the navigation stays on the left, and the main content takes the remaining space.
  - The body has `overflow: hidden` to ensure there is no vertical scrollbar for the page.
  - The container uses `calc(100vh - 150px)` to ensure that the margins fit correctly.

## Recommendations:
- Consider adding media queries/links to improve usefulness
