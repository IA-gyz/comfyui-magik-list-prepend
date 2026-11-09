# Magik List Prepend

Extract `magik_list_prepend` into `ComfyUI/custom_nodes/` and restart ComfyUI.
Find **Magik List Prepend** under **Magik/Text**. No additional dependencies.

Inputs (ComfyUI socket types in parentheses):
- **Text List** (`STRING` list): connect an upstream string-list output.
- **Add** (`STRING`): exact prefix. Dynamic prompt expansion is disabled.
- **Quadrants** (optional `INT` list): connect Magik Where Is The Face's integer-list output.

The input sockets use ComfyUI's standard STRING and INT types. `INPUT_IS_LIST`
receives the entire execution list; `OUTPUT_IS_LIST` returns a real string list.

Indices are **1-based**: 1 selects the first string, 2 the second, etc.
The node uses list positions, so arrange Text List in your quadrant order.
Unconnected Quadrants selects all strings; a connected empty list selects none.
Duplicate indices apply the prefix only once. Out-of-range indices are ignored.
Output order and length are preserved. Inputs are not modified.
No separator is inserted automatically; include one in Add if desired.
Add must supply one string, including when supplied through a connection.

Example:

```text
Text List = ["top left", "top right", "bottom right", "bottom left"]
Quadrants = [1, 3]
Add = "face, "
Prep Text = ["face, top left", "top right", "face, bottom right", "bottom left"]
```
