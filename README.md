# ML2


### **1. Clone the Repository**
1. **Install Git** (if not already installed):
   - [Download Git](https://git-scm.com/downloads) and set it up on your machine.
2. **Open VSCode**:
   - Go to **View > Command Palette** or press `Ctrl + Shift + P`.
   - Search for `Git: Clone` and select it.
3. **Provide the Repository URL**:
   - Paste the GitHub repository URL (HTTPS or SSH) and press `Enter`.
4. **Select a Folder**:
   - Choose a folder on your local machine where the repository will be cloned.
5. **Open the Project**:
   - When prompted, open the cloned repository in VSCode.

---

### **2. Create a New Branch**
1. **Open the Branch Menu**:
   - In the bottom-left corner of VSCode, click the branch name (e.g., `main`).
2. **Create a New Branch**:
   - Select **Create new branch**.
   - Enter a name for your new branch (e.g., `feature-xyz`) and press `Enter`.
3. **Switch to the New Branch**:
   - After creating the branch, VSCode will automatically switch to it. If not, manually select it from the branch menu.

---

### **3. Make Changes and Commit**
1. **Edit Files**:
   - Make the necessary changes to the files in the project.
2. **Stage Changes**:
   - Go to the **Source Control** view (icon with three branches) or press `Ctrl + Shift + G`.
   - Click the `+` icon next to the files you’ve modified to stage them.
3. **Commit Changes**:
   - In the message box, write a meaningful commit message (e.g., `Add new feature`) and press `Ctrl + Enter`.

---

### **4. Push the Branch to GitHub**
1. **Push the Branch**:
   - Open the terminal in VSCode (`Ctrl + ~`) and run:
     ```bash
     git push -u origin <branch-name>
     ```
     Replace `<branch-name>` with the name of your branch.
2. **Verify on GitHub**:
   - Go to the GitHub repository page to ensure your branch appears in the list.

---

### **5. Create a Pull Request (PR)**
1. **Navigate to the Repository on GitHub**:
   - Open the repository in your browser.
2. **Create a Pull Request**:
   - Click **Pull Requests** > **New Pull Request**.
   - Select your branch as the source and `main` (or the target branch) as the destination.
   - Add a title, description, and reviewers if needed, then submit the PR.

---

### **6. Collaborate on the Project**
1. **Fetch Updates Regularly**:
   - Keep your branch up to date with the latest changes from the main branch:
     ```bash
     git fetch origin
     git merge origin/main
     ```
2. **Resolve Conflicts**:
   - If conflicts occur during merging, VSCode will highlight them in the editor. Resolve the conflicts, stage the files, and complete the merge.
3. **Pull Changes from Others**:
   - If others push updates to the repository, pull the changes into your branch:
     ```bash
     git pull origin <branch-name>
     ```

