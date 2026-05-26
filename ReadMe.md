//Produced By Wu Guanyu Productions, All Rights Reserved.

**Storyline Blueprint Editor User Manual**

**Version:** 1.0
**Target Audience:** Game Narrative Designers, Copywriters, Level Designers

---

### 1. Introduction
This software is a node-based storyline blueprint editor specifically designed for game narrative designers and writers. Designers can quickly build complex branching narrative logic, dialogue choices, and cinematic transition controls through visual node connections. The software features a highly convenient bidirectional conversion between a "Script Table" and a "Node Blueprint." It also provides comprehensive multilingual localization support and a real-time storyline simulation sandbox. The final output can be directly exported as data tables or JSON files for game engine integration.

---

### 2. Interface Layout Overview
Upon launching the software, the system is divided into two core interfaces: the **Story Management List (Main Interface)** and the **Blueprint Editing Workspace**.

#### 2.1 Story Management List
*   **Left List Area:** Displays all storyline files within the current project and marks recently opened projects.
*   **Right Operation Area:** Contains global operation buttons including Interface Language Toggle (EN/CN), New, Open, Rename, Save As, Export Table, Enter Script Editor, and Delete Storyline.

#### 2.2 Blueprint Editing Workspace
Double-click any project in the story list to enter the blueprint workspace. The interface is divided into the following areas:
*   **Top Toolbar:** Contains Return to List, Run Mode Toggle (Auto/Manual), Playback Language Selection, Run/Stop Controls, Back to Start Node, Localization Management, and Save/Export operations.
*   **Central Blueprint Canvas:** An infinitely zoomable grid workspace used for creating, connecting, and arranging various narrative logic nodes.
*   **Bottom-Left Playback Preview Bar:** During narrative simulation, this area prints the content of the currently active node in real-time (in a script dialogue format) and provides clickable interactions for branching options.
*   **Right Property Panel:** When any node on the canvas is selected, this panel displays all detailed parameters of that node, supporting real-time modifications and multilingual text input.

---

### 3. Basic Project and Localization Management

#### 3.1 Creating and Saving Storylines
*   **New:** Click "New Storyline" on the main interface and enter a name to create a blank blueprint.
*   **Save and Exit:** In the blueprint workspace, click "Save Storyline" to save current modifications. If you attempt to click "Return to Story List" or close the software without saving, the system will prompt a confirmation dialog to prevent data loss.

#### 3.2 Managing Multilingual Support (Localization)
To accommodate global game publishing, the software features built-in multilingual management:
1.  Click the "Manage Localization" button at the top of the blueprint workspace.
2.  In the pop-up dialog, enter the required language code (e.g., English, JP) and click confirm to add it.
3.  Once added, a "Select Language" dropdown menu will appear above the text input boxes in the property panel, allowing you to enter dialogue or option scripts for different languages.

---

### 4. Node and Blueprint Basic Operations

#### 4.1 Node Creation and Selection
*   **Create Node:** Right-click on an empty space in the central canvas and select the desired node type from the context menu.
*   **Select Node:** Left-click any node to select it. The selected node's border will highlight in gold. Click and hold the left mouse button on an empty space and drag to box-select multiple nodes.

#### 4.2 Connections and Logic Flow
*   **Establish Connection:** Each node has circular ports on its left and right sides. The left is the input port, and the right is the output port. Left-click and hold an output port, drag to draw a connection line, and drop it onto the input port of the next node.
*   **Infinite Loop Prevention:** The system has built-in loop detection. If your connection would cause the narrative logic to enter an infinite loop, the system will reject the operation and issue a warning.
*   **Delete Connection:** Select a connection line and press the `Delete` key, or right-click and select "Delete Connection". You can also hold the `Ctrl` key and click a port to quickly clear all connections on that port.

#### 4.3 View Navigation
*   **Pan Canvas:** Hold down the middle mouse button and drag to pan the current view.
*   **Zoom Canvas:** Scroll the mouse wheel to zoom in and out of the canvas.
*   **Reset View:** Click the "Back to Start" button at the top, and the camera will instantly center and align to the "Start" node.

---

### 5. Node Types and Property Panel Details
Each node carries a different narrative function. When selected, its parameters can be configured in the right panel:

*   **Start:**
    *   Every blueprint must contain exactly one of these nodes. It is the sole entry point for storyline execution and exporting.
*   **Dialogue:**
    *   **Core Fields:** Scene Number, Dialogue ID, Speaker, Emotion, Camera Shot, Scene Description, and Dialogue Script (multilingual supported).
    *   **Notes:** Additional designer remarks. The input text will appear as a floating bubble above the node on the canvas. The visibility of the bubble can be adjusted via the "Note Opacity" slider.
    *   **Playback Duration:** The number of seconds the dialogue remains on screen during auto-run mode.
*   **Branch (Dialogue Options):**
    *   Used to build player choices. Click "Add Branch (+)" in the panel to add new options.
    *   Each option can be independently configured with option text (multilingual supported), associated Scene Number, Dialogue ID, and notes.
    *   As options are added, corresponding output ports are automatically generated on the right side of the node to connect subsequent narrative branches.
*   **Scene Prompt:**
    *   Used to output voiceovers or scene action descriptions without a specific speaker.
*   **Note:**
    *   Used purely for visual logic grouping and explanation on the canvas. It does not affect the actual game flow export. Font colors can be modified for visual distinction.
*   **Transition:**
    *   Defines visual transition effects between narrative scenes. You can set "Fade In/Fade Out" and the duration of the transition.
*   **Jump Start / Jump End:**
    *   When a blueprint becomes extremely massive, direct wiring can cause canvas clutter.
    *   By setting identical "Jump Identifiers" (e.g., "Plot Point A"), a "Jump Start" and "Jump End" can be logically connected seamlessly without drawing an actual line.

---

### 6. Story Playback and Debugging
The software includes a real-time simulator to verify narrative coherence before delivering data to the engine.

#### 6.1 Run Mode
*   **Auto Run:** The system automatically advances the story in sequence based on the "Playback Duration" set in the nodes.
*   **Manual Run:** The system pauses after each node. Click anywhere inside the "Playback Preview Bar" at the bottom left to manually advance to the next step.

#### 6.2 Real-time Preview and Localization Testing
*   Select the "Playback Language" from the top toolbar (defaults to the base language, but you can select added languages like English).
*   Click "Start Run". The story will be printed line-by-line in a script format in the bottom-left preview bar.
*   If the execution reaches a "Branch" node, the preview bar will pause and display clickable buttons. Clicking a button will route the playback into the corresponding narrative branch.
*   **Missing Localization Warning:** During playback, if the system detects that text is missing for the currently selected playback language on a node, it will output a yellow warning and automatically halt execution.

#### 6.3 Error Validation and Breakpoint Debugging
*   **Syntax Check:** Upon clicking Run, the system performs a full scan. If there are issues like "Empty Dialogue ID," "Playback Duration is 0," or "Jump Identifier cannot find an endpoint," the problematic node will turn entirely red, and an error list will pop up prompting corrections.
*   **Duplication Check:** If the system detects duplicate nodes with identical "Scene Number" and "Dialogue ID," it will immediately pop up a warning and highlight the duplicate nodes in red.
*   **Breakpoint:** Right-click a node and select "Toggle Breakpoint" (or select it and press `Ctrl + T`). A red dot will appear in the top-right corner of the node. In Auto Run mode, execution will forcefully pause upon reaching this node, aiding in branch flow inspection.

---

### 7. Script Editor (Advanced Bidirectional Workflow)
For writers accustomed to using Excel, the software provides a spreadsheet-like rapid data entry interface. Click "Script Editor" on the main interface to access it.

#### 7.1 Table Operations
*   This interface uses a standard row-and-column layout. Manage data via the "Add Row" and "Delete Row" buttons at the top.
*   The first column is the "Function Type" (Dialogue Node, Branch Option, Transition, etc.), followed by Scene Number, Speaker, and various localization script columns.
*   Supports batch copying from external Excel/CSV files. Simply press `Ctrl + V` inside the table, and the system will automatically expand downwards and populate the data.
*   **Real-time Duplication Check:** When modifying Scene Numbers and Dialogue IDs in the table, if a duplicate is created, the corresponding row's background will immediately turn dark red.

#### 7.2 Bidirectional Conversion between Table and Blueprint
*   **Import from Blueprint:** Click the top button to select an existing blueprint file. The system will automatically flatten it into table content based on the node connection sequence, making it easy to proofread text centrally.
*   **One-Click Convert to Blueprint Outline:** After completing table entry, click this button. The system will automatically convert all rows into visual nodes in sequence, wire them up, bind branches, and generate a brand-new blueprint storyline. This massively boosts output efficiency during the whitebox phase.
*   **Import/Export:** The table supports exporting as standalone `.xlsx` or `.csv` formats for external circulation.

---

### 8. Data Export
Once editing is complete, the design data must be exported for programmers and the game engine to read.
1.  **Export as Storyline (JSON):**
    Saves all node coordinates, connection logic, and attributes, generating a pure code format file. This is typically parsed directly by the game engine as a narrative configuration file.
2.  **Export as Table (Excel/CSV):**
    The system flattens the entire tree structure according to the node traversal sequence and exports it as a standard master dialogue sheet. This includes complete base language and added localization columns, which can be directly handed over to the audio department as a voiceover recording reference.
    *Note: Exporting to .xlsx format requires a local Python environment with pandas and openpyxl libraries installed. Otherwise, the system will prompt a warning and suggest downgrading the export to .csv format.*

---

### 9. Shortcut List
To improve editing efficiency, the blueprint workspace supports the following shortcut operations:
*   **Undo:** `Ctrl + R` (Undoes the previous node modification or connection)
*   **Copy Selected Node:** `Ctrl + C`
*   **Cut Selected Node:** `Ctrl + X`
*   **Paste Node:** `Ctrl + V` (Pastes at the current mouse cursor location)
*   **Duplicate in Place:** `Ctrl + D` (Copies the selected node and quickly spawns it to the bottom-right of the original)
*   **Delete Selected Item:** `Delete`
*   **Toggle Breakpoint:** `Ctrl + T`
*   **Quick Clear Port Connections:** While in a connecting state, hold `Ctrl` and click a node's input/output port.
