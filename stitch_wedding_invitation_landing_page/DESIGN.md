# Design System Document

## 1. Overview & Creative North Star: "The Digital Keepsake"
This design system is built to transform a standard wedding invitation into a high-end editorial experience. The "Creative North Star" is **The Digital Keepsake**—a philosophy that treats the web browser not as a software interface, but as a piece of fine stationery. 

To achieve this, the system breaks away from the rigid, "boxy" layout of typical web apps. We utilize **intentional asymmetry**, allowing floral elements to bleed off-canvas and typography to overlap subtle background shifts. We prioritize **white space as a luxury material**, using the expansive `surface` and `surface-container` tiers to create a breathing, celebratory atmosphere that feels curated rather than templated.

---

## 2. Colors: Tonal Depth & Warmth
The palette is rooted in the romance of traditional print. It uses high-contrast accents of Deep Red against a warm, layered neutral base.

*   **Foundation:** The `background` (`#fbf9f5`) and `surface` tiers provide a creamy, organic feel, moving away from the clinical "stark white" of digital screens.
*   **The Burgundy Accent:** The `primary` (`#640013`) is reserved for the most important emotional moments—names of the couple, ceremonial headings, and primary calls to action (RSVP).
*   **The "No-Line" Rule:** We strictly prohibit the use of 1px solid borders to define sections. Layout boundaries must be created through background color shifts. For example, a section detailing the venue might sit on `surface-container-low` to distinguish it from the `surface` hero section.
*   **Glass & Gradient Rule:** For floating elements like sticky navigation or RSVP modals, use Glassmorphism. Apply `surface` with 80% opacity and a `backdrop-filter: blur(12px)`. To add "soul" to buttons, use a subtle linear gradient from `primary` to `primary_container` (`#8d021f`).

---

## 3. Typography: Editorial Sophistication
Typography is the primary driver of the invitation’s elegance. We pair a timeless serif with a modern, breathable sans-serif.

*   **Display & Headline (Noto Serif):** Used for "Lễ Thành Hôn," the couple's names, and section titles. These should utilize generous letter-spacing and, where appropriate, `italic` styling to mimic calligraphy.
*   **Body & Labels (Plus Jakarta Sans):** A clean, high-legibility sans-serif used for addresses, dates, and logistical details. This provides a functional counter-point to the romantic serif.
*   **Hierarchy as Identity:** 
    *   `display-lg`: Reserved for names and the main event title.
    *   `title-md`: Used for labels like "NHÀ TRAI" or "NHÀ GÁI," often in uppercase with `0.1rem` tracking to evoke a premium feel.

---

## 4. Elevation & Depth: Tonal Layering
In a "Digital Keepsake," depth should feel like stacked sheets of premium cardstock, not like a computer window.

*   **The Layering Principle:** Avoid shadows for static layout components. Instead, place a `surface-container-lowest` card on top of a `surface-container-low` background. This creates a "soft lift" that feels natural and tactile.
*   **Ambient Shadows:** If a component must float (e.g., a photo gallery light-box), use an extra-diffused shadow. 
    *   *Specification:* `box-shadow: 0 20px 50px rgba(89, 65, 64, 0.06);`. The shadow color is a tint of `on_surface_variant`, making it feel like ambient light rather than a gray smudge.
*   **The Ghost Border:** If a form field or container requires a boundary for accessibility, use the `outline_variant` at 20% opacity. Never use a 100% opaque border.

---

## 5. Components: Intentional Minimalism

### Buttons
*   **Primary:** Solid `primary` background with a subtle gradient to `primary_container`. Roundedness set to `full` to contrast against the editorial layout.
*   **Tertiary:** Typography only (`title-sm`), using `primary` color with a custom underline that sits 4px below the text.

### Cards & Event Details
*   **Structure:** Forbid divider lines. Use vertical white space (Spacing `8` or `12`) to separate information.
*   **Visual Treatment:** Cards should have no border. Use a background of `surface_container_lowest` and a `xl` (0.75rem) corner radius.

### Input Fields (RSVP)
*   **Style:** Minimalist. No box. Only a bottom border using `outline_variant` at 40% opacity.
*   **Focus State:** The bottom border transitions to `primary` with a smooth 300ms ease.

### Decorative Elements (Custom)
*   **Watercolor Accents:** Subtle `surface_tint` or floral PNGs should be positioned using `absolute` coordinates, often breaking the "grid" by overlapping text and container edges to create a sense of hand-crafted artistry.

---

## 6. Do's and Don'ts

### Do:
*   **Use Asymmetry:** Place the "Date" on the left and "Location" slightly offset to the right. A rigid center-align-everything approach feels like a template.
*   **Animate Transitions:** Use `cubic-bezier(0.22, 1, 0.36, 1)` for all fade-ins. Elements should "float" into place as the user scrolls.
*   **Leverage White Space:** If in doubt, add more space. The `spacing-20` (7rem) token is your friend for separating major sections.

### Don't:
*   **Don't use 100% Black:** Always use `on_surface` (#1b1c1a) for text. Pure black is too harsh for the "Digital Keepsake" aesthetic.
*   **Don't use Standard Shadows:** Avoid the "Material Design" default floating action button shadows. They are too aggressive for a romantic wedding theme.
*   **Don't use Dividers:** Never use `<hr>` or solid lines to separate content. Use the tonal shifts between `surface-container` tiers.