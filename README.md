<snippet>
<content>

# ![Alt](./app_icon_and_logo.png "Check Student Loans"): Other Resources

This project consists of other resources. These resources supplement the course material or native app.<p>

Alternative downloads:<br>
[Version 1.x for Feasibility Test](./Archives/feasibility_test.zip "Click here to access the download link.")<br>
[Version 1.x for Formal Pilot Test](./Archives/formal_pilot_test.zip "Click here to access the download link.")<br>
[Version 1.x for Informal Pilot Test](./Archives/informal_pilot_test.zip "Click here to access the download link.")<br>
[Version 1.x for Focus Groups](./Archives/focus_groups.zip "Click here to access the download link.")<br>
[Version 1.x for Panel Discussion](./Archives/panel_discussion.zip "Click here to access the download link.")<br>
[Version 1.6.1 - Summative Copy](./Archives/summative_copy.zip "Click here to access the download link.")<p>
<!--[Version 2.7.2 - Latest](./Archives/latest-2_7_2.ipa "Click here to access the download link.") (Updated: August 16, 2019)<p>-->
"Unzip" the bundle, then open each PDF file with [Acrobat Reader DC](https://acrobat.adobe.com/us/en/acrobat/pdf-reader.html "Click here to access the download link.").

## Build from Source Code

Clone the project:
<pre>
$ git clone https://gitlab.com/saegl5/check-student-loans-other-resources.git
</pre>

(Recommended) Verify the project's authenticity: Look for "Verified" next to the commit SHA (e.g., Verified e733a45d).

(Recommended) Open a terminal, and verify the project's integrity:
<pre>
$ cd /path/to/check-student-loans-other-resources
$ git show-ref --heads --hash
</pre>
Check that the hash matches the commit SHA.<p>

### introductory_script.md

>&nbsp;<br>
>Open and edit "introductory_script.md" with a text editor (e.g., Notepad, TextEdit or gedit).<p>
>Then, convert it to a Microsoft Word document.<br>
>To convert the file, install [Pandoc](https://pandoc.org/ "Click here for more information.") and open a terminal:
>```
>$ pandoc --lua-filter gitlab-math.lua -s introductory_script.md -o introductory_script.docx
>```
>Afterward, open "introductory_script.docx" with Microsoft Word.<br>
>&nbsp;

### iOS_app_overview.md

>&nbsp;<br>
>Open and edit "iOS_app_overview.md," and convert it to a Microsoft Word document, as done similarly above. Then, open "iOS_app_overview.docx" with Microsoft Word.<br>
>&nbsp;

### checklist_for_checking_calculations.docx

>&nbsp;<br>
>Open and edit "checklist_for_checking_calculations.docx" with Microsoft Word.<br>
>&nbsp;

### checking_calculations.xlsx

>&nbsp;<br>
>Open and edit "checking_calculations.xlsx" with Microsoft Excel.<br>
>&nbsp;

The markdown files', document's and spreadsheet's latest version is 1.6.1. The Lua filter requires Pandoc version 2.0 or higher. Known to work on Windows 10 Pro version 1903, in Microsoft Word for Office 365 version 1908 (64-bit)

## Usage

Instructors follow the introductory script and can keep the app overview for their personal reference.
[Course material](https://gitlab.com/saegl5/check-student-loans-course-material "Click here to access the course material repository.") is distributed to students for them to complete.
However, instructors should not simply hand them the material; they should illustrate some examples briefly.
Students answer some questions in the course material with the native app, some not.
On how to proceed from there is the instructor's discretion.

<!-- ### Alternative Build Method for Markdown

Install Pandoc *and* [R](https://www.r-project.org "Click here for more information."); open a terminal; then, use R to render the file as a Microsoft Word document: (R utilizes Pandoc in the background)
```
$ R
> install.packages("rmarkdown")
> library(rmarkdown)
> render("introductory_script.md") # example
``` 
The benefit to rendering markdown with R is that one can embed executable R [code chunks](https://rmarkdown.rstudio.com/lesson-3.html "Click here for more information."). Embed a chunk; change the file's extension to .Rmd; then, re-render the file. -->

### Additional Resources

special_cases_in_iOS.txt<br>
(one for rounding to the nearest cent, and one for casting as an integer)


Jupyter > Ten-Year_Minimum_Errors.ipynb<br>
(for computing ten-year minimum monthly payment errors)

LaTeX > deeper_insight.pdf<br>
(provides context, an overview, terminology and formulae)

LaTeX > extra_insight.pdf<br>
(provides examples and derivations)

<!--deeper_insight.tex (source code)
    extra_insight.tex (source code)
    images/ (images for deeper_insight.pdf)
    images/svg/ (source of images for deeper_insight.pdf)-->

## Contributing

Sign into GitLab, to fork the project.<p>

Modify any resources.<br>
Under Source Control, select Commit, and Push the changes.<p>

Return to GitLab, and submit a new pull request.<br>
For any issues, submit a new issue or discuss an existing one.<p>

## History

Sep 24-28, 2019 &middot; Version 1.6.1: extracted some resources from the "course material" repository into a newly separate repository, added extension to rounding_notes, renamed rounding_notes, archived the resources<br>
Aug 27, 2019 &middot; Version 1.6: updated interest rate and default numbers, aligned how savings and change in savings are calculated and displayed<br>
Aug 20, 2019 &middot; Version 1.5: reorganized resources again, corrected spreadsheet<br>
Aug 8, 2019 &middot; Version 1.4: reorganized resources, provided raw files for images, added READMEs<br>
Jul 29-Aug 5, 2019 &middot; Version 1.3: uploaded Ten-Year_Minimum_Errors.ipynb, updated other documents<br>
Jul 2-6, 2019 &middot; Version 1.2.2: split deeper_insight.docx into two documents, typeset them in LaTeX, uploaded each pdf produced from each TeX source, revised checking_calculations.xlsx, updated overview<br>
Jul 10-11, 2018 &middot; Version 1.2.1: updated documents<br>
Jun 21, 2018 &middot; Version 1.2: redid deeper_insight.docx<br>
Jun 13-15, 2018 &middot; Version 1.1.1: updated Word documents, reorganized resources, added README<br>
Mar 27, 2018 &middot; Version 1.1: updated Word documents<br>
Mar 21-22, 2018 &middot; Version 1: initial uploads

<!--## Known Issues

Video introduction does not render correctly, if installed from the App Store.<br>
Potential Xcode bug: Unlike for plain text, for attributed text the interface builder draws custom fonts from Font Book.-->

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

</content>
</snippet>
