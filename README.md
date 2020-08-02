![Alt](./app_icon_and_logo.png "Check Student Loans")

## Other Resources

This project consists of other resources. These resources supplement the [course material](https://gitlab.com/check-student-loans/course-material "Click here to access the course material repository."), [native app](https://gitlab.com/check-student-loans/ios "Click here to access the native app's repository.") or each other.

Alternative downloads: \
[Version 1.x for Feasibility Test](https://gitlab.com/check-student-loans/other-resources/-/blob/66f4a864b77457d62247b1f405cdc07aaf4bd29a/Archives/feasibility_test.zip "Click here to access the download link.") \
[Version 1.x for Formal Field Test](https://gitlab.com/check-student-loans/other-resources/-/blob/66f4a864b77457d62247b1f405cdc07aaf4bd29a/Archives/formal_field_test.zip "Click here to access the download link.") \
[Version 1.x for Informal Field Test](https://gitlab.com/check-student-loans/other-resources/-/blob/66f4a864b77457d62247b1f405cdc07aaf4bd29a/Archives/informal_field_test.zip "Click here to access the download link.") \
[Version 1.x for Focus Groups](https://gitlab.com/check-student-loans/other-resources/-/blob/66f4a864b77457d62247b1f405cdc07aaf4bd29a/Archives/focus_groups.zip "Click here to access the download link.") \
[Version 1.x for Panel Discussion](https://gitlab.com/check-student-loans/other-resources/-/blob/66f4a864b77457d62247b1f405cdc07aaf4bd29a/Archives/panel_discussion.zip "Click here to access the download link.") \
[Version 1.6.4 - Summative Copy](https://gitlab.com/check-student-loans/other-resources/-/blob/017832daf00664e02e112591884c016ac25c2379/Archives/summative.zip "Click here to access the download link.") \
[Version 1.6.4 - Latest](https://gitlab.com/check-student-loans/other-resources/-/blob/017832daf00664e02e112591884c016ac25c2379/Archives/latest.zip "Click here to access the download link.") (Aug 2, 2020)

"Unzip" the bundle, then...

Open the IPYNB file with SageMath Notebook. \
Open the XLSX file with Microsoft Excel. \
Open the DOCX file with Microsoft Word. \
Open each PDF file with [Acrobat Reader DC](https://acrobat.adobe.com/us/en/acrobat/pdf-reader.html "Click here to access the download link."). \
Open the TXT file with a text editor (e.g., Notepad, TextEdit or gedit).

## Build from Source Code

Download and install [Pandoc](https://pandoc.org/ "Click here for more information.") and [Git](https://git-scm.com/downloads "Click here to access the download link.").

Open a terminal, and clone the project:
```
git clone https://gitlab.com/check-student-loans/other-resources.git
```

(Recommended) Verify the project's authenticity: Look upward for "Verified," next to the commit SHA.

(Recommended) Open a terminal, and verify the project's integrity:
```
cd other-resources
git show-ref --heads --hash
```
Check that the hash matches the commit SHA.

### introductory_script.md<br />(supplements the course material)

>Open and edit "introductory_script.md" with a text editor (e.g., Notepad, TextEdit or gedit).
>
>Then, convert it to a Microsoft Word document. \
>To convert the file, and open a terminal:
>```
>pandoc --lua-filter gitlab-math.lua -s introductory_script.md -o introductory_script.docx
>```
>Afterward, open "introductory_script.docx" with Microsoft Word.

### iOS_app_overview.md<br />(supplements the course material)

>Open and edit "iOS_app_overview.md," and convert it to a Microsoft Word document, as done similarly above. Then, open "iOS_app_overview.docx" with Microsoft Word.

### checklist_for_checking_calculations.docx<br />(supplements the native app)

>Open and edit "checklist_for_checking_calculations.docx" with Microsoft Word.

### checking_calculations.xlsx<br />(supplements the native app)

>Open and edit "checking_calculations.xlsx" with Microsoft Excel.

The Lua filter requires Pandoc version 2.0 or higher.

## Usage

Instructors follow the introductory script and can keep the app overview for their personal reference.
[Course material](https://gitlab.com/check-student-loans/course-material "Click here to access the course material repository.") is distributed to students for them to complete.
However, instructors should not simply hand them the material; they should illustrate some examples briefly.
Students answer some questions in the course material with the native app, some not.
On how to proceed from there is the instructor's discretion.

<!-- ### Alternative Build Method for Markdown

Install Pandoc *and* [R](https://www.r-project.org "Click here for more information."); open a terminal; then, use R to render the file as a Microsoft Word document: (R utilizes Pandoc in the background)
```
R
> install.packages("rmarkdown")
> library(rmarkdown)
> render("introductory_script.md") # example
``` 
The benefit to rendering markdown with R is that one can embed executable R [code chunks](https://rmarkdown.rstudio.com/lesson-3.html "Click here for more information."). Embed a chunk; change the file's extension to .Rmd; then, re-render the file. -->

## Additional Resources

special_cases_in_iOS.txt \
(one for rounding to the nearest cent, and one for casting as an integer; supplements the native app)


Jupyter > Ten-Year_Minimum_Errors.ipynb \
(for computing ten-year minimum monthly payment errors; supplements checking_calculations.xlsx *and* the native app)

LaTeX > deeper_insight.pdf \
(provides context, an overview, terminology and formulae; supplements checking_calculations.xlsx *and* the native app)

LaTeX > extra_insight.pdf \
(provides examples and derivations; supplements checking_calculations.xlsx *and* the native app)

<!--deeper_insight.tex (source code)
    extra_insight.tex (source code)
    images/ (images for deeper_insight.pdf)
    images/svg/ (source of images for deeper_insight.pdf)-->

## Contributing

Sign into GitLab, and fork the project.

Modify any resources. \
Stage, commit and push the changes.

Return to GitLab, and submit a new pull request. \
To report any issues, submit a new issue or discuss an existing one.

## History

Aug 2, 2020 &middot; Version 1.6.4: proofread deeper_insight.tex \
Mar 24, 2020 &middot; Version 1.6.3: changed "Jupyter Notebook or Jupyter Lab" to "SageMath Notebook" \
Nov 30, 2019 &middot; Version 1.6.2: fixed latex images \
Sep 25, 2019: unified author name and email of all commits \
Sep 24-28, 2019 &middot; Version 1.6.1: extracted some resources from the "course material" repository into a newly separate repository, added extension to rounding_notes, renamed rounding_notes, archived the resources \
Aug 27, 2019 &middot; Version 1.6: updated interest rate and default numbers, aligned how savings and change in savings are calculated and displayed \
Aug 20, 2019 &middot; Version 1.5: reorganized resources again, corrected spreadsheet \
Aug 8, 2019 &middot; Version 1.4: reorganized resources, provided raw files for images, added README files \
Jul 29-Aug 5, 2019 &middot; Version 1.3: uploaded Ten-Year_Minimum_Errors.ipynb, updated other documents \
Jul 2-6, 2019 &middot; Version 1.2.2: split deeper_insight.docx into two documents, typeset them in LaTeX, uploaded each pdf produced from each TeX source, revised checking_calculations.xlsx, updated overview \
Jul 10-11, 2018 &middot; Version 1.2.1: updated documents \
Jun 21, 2018 &middot; Version 1.2: redid deeper_insight.docx \
Jun 13-15, 2018 &middot; Version 1.1.1: updated Word documents, reorganized resources, added README \
Mar 27, 2018 &middot; Version 1.1: updated Word documents \
Mar 21-22, 2018 &middot; Version 1: initial uploads

<!--## Known Issues

Video introduction does not render correctly, if installed from the App Store. \
Potential Xcode bug: Unlike for plain text, for attributed text the interface builder draws custom fonts from Font Book.-->

## License

Creative Commons Attribution 4.0 International