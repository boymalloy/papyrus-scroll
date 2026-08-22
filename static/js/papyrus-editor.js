/*
 * Papyrus Scroll extensions for Toast UI Editor.
 *
 * This file contains Papyrus-specific editor behaviour.
 * Keeping it separate means that future features can be added here
 * without making the HTML template increasingly complicated.
 */


/*
 * Sphinx cross-reference:
 *
 *     {ref}`Interchange`
 */
const sphinxReferencePattern = /\{ref\}`([^`]+)`/;


/*
 * Sphinx target:
 *
 *     (Interchange)=
 */
const sphinxTargetPattern = /\(([^()\n]+)\)=/;


/*
 * Converts a Sphinx reference into a clickable editor widget.
 */
function createReferenceWidget(text) {
    const match = text.match(sphinxReferencePattern);

    if (!match) {
        return document.createTextNode(text);
    }

    const targetName = match[1];

    const link = document.createElement("a");

    link.className = "papyrus-reference";
    link.href = `#papyrus-target-${makeSafeId(targetName)}`;
    link.dataset.target = targetName;
    link.textContent = targetName;
    link.title = `Reference to: ${targetName}`;

    return link;
}


/*
 * Converts a Sphinx target into a visible target marker.
 */
function createTargetWidget(text) {
    const match = text.match(sphinxTargetPattern);

    if (!match) {
        return document.createTextNode(text);
    }

    const targetName = match[1];

    const target = document.createElement("span");

    target.className = "papyrus-target";
    target.id = `papyrus-target-${makeSafeId(targetName)}`;
    target.dataset.target = targetName;
    target.textContent = `Target: ${targetName}`;
    target.title = `Sphinx target: (${targetName})=`;

    return target;
}


/*
 * Converts a target name into something safe to use as an HTML id.
 */
function makeSafeId(value) {
    return value
        .trim()
        .toLowerCase()
        .replace(/[^a-z0-9_-]+/g, "-")
        .replace(/^-+|-+$/g, "");
}


/*
 * These are the Papyrus-specific Toast UI widget rules.
 */
const papyrusWidgetRules = [
    {
        rule: sphinxReferencePattern,

        toDOM(text) {
            return createReferenceWidget(text);
        }
    },
    {
        rule: sphinxTargetPattern,

        toDOM(text) {
            return createTargetWidget(text);
        }
    }
];


/*
 * Returns the standard Toast UI settings used by Papyrus Scroll.
 *
 * Extra settings can be supplied by the page that creates the editor.
 */
function createPapyrusEditorOptions(options = {}) {
    return {
        height: "500px",
        initialEditType: "wysiwyg",
        previewStyle: "vertical",
        widgetRules: papyrusWidgetRules,

        ...options
    };
}