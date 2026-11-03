# VPS learning materials

## Built visual system

Reader mode: a daylight-friendly technical field manual, using a pale blue-white ground, dark blue text and a restrained blue link/interaction accent. System typography avoids external font downloads. Wide pages support a two-column introduction; lessons retain a narrow reading measure. Small screens stack content and request-path steps.

Shared tokens and components live in `assets/course.css`: reading layout, request path, reference tables, warning/note blocks, quiz forms, disclosure answers and print rules. Motion is limited to scrolling and disabled with reduced-motion preferences. Native radio inputs, labeled options, focus indicators, skip links and live status feedback preserve familiar interaction.

## Responsive navigation

All three pages share a top navbar with a current-page marker and a left sidebar containing learning links and page-specific contents. Desktop navigation is sticky and independently scrollable; below 901px the sidebar becomes an in-flow native disclosure, avoiding overlays and focus traps. JavaScript sets the initial disclosure state, responds to breakpoint changes, closes after selection, and supports Escape with focus returned to its summary. Without JavaScript the disclosure starts open and remains operable. Anchor targets are focusable for keyboard continuation. Print hides navigation and restores the single-column reading layout.

The existing palette, content and typography remain unchanged. Narrow layouts stack introductory columns and request-path steps; tables wrap within the reading column. No navigation framework or dependency was added.

## Verification and limits

Static checks cover all local links/anchors, navigation landmarks, current-page markers and quiz structure. Node tests cover feedback and menu behavior. Firefox checks cover all three pages at 320, 768 and 1440 CSS pixels (using an iframe below Firefox's minimum window width), no horizontal overflow, native keyboard opening and TOC click/focus. Desktop and mobile screenshots were inspected. Original content received a separate safety/correctness source review. No assistive-technology, real-device, cross-browser or PDF-print review was performed.

No generated imagery, remote runtime assets, persistent progress tracking or provider connections are shipped.
