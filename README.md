<snippet>
<content>

# ![Alt](./app_icon_and_logo.png "Check Student Loans"): Resources

This project consists of course material and other resources. The course material is one of two parts of an experimental study&mdash;the other part being a [native app](https://gitlab.com/saegl5/check-student-loans-for-ios "Click here to access the native app's repository."), and it is designed to be supplemented by the native app.
The combination of both parts is dubbed an *instructional app*.<p>

Alternative downloads:<br>
[Version 1.x for Feasibility Test](./Archives/feasibility_test.pdf "Click here to access the download link.")<br>
[Version 1.x for Formal Pilot Test](./Archives/formal_pilot_test.pdf "Click here to access the download link.")<br>
[Version 1.x for Informal Pilot Test](./Archives/informal_pilot_test.pdf "Click here to access the download link.")<br>
[Version 1.x for Focus Groups](./Archives/focus_groups.pdf "Click here to access the download link.")<br>
[Version 1.x for Panel Discussion](./Archives/panel_discussion.pdf "Click here to access the download link.")<br>
[Version 1.7.1 - Summative Copy](./Archives/summative_copy.pdf "Click here to access the download link.")<p>
<!--[Version 2.7.2 - Latest](./Archives/latest-2_7_2.ipa "Click here to access the download link.") (Updated: August 16, 2019)<p>-->
Open each PDF file with Acrobat Reader DC (https://acrobat.adobe.com/us/en/acrobat/pdf-reader.html).

## Build from Source Code

Clone the project:
<pre>
$ git clone https://gitlab.com/saegl5/check-student-loans-resources.git
</pre>

(Recommended) Verify the project's authenticity: Look for "Verified" next to the commit SHA (e.g., Verified e733a45d).

(Recommended) Open a terminal, and verify the project's integrity:
<pre>
$ cd /path/to/check-student-loans-resources
$ git show-ref --heads --hash
</pre>
Check that the hash matches the commit SHA.<p>

Edit "latest.md," then convert it to a Microsoft Word document. The file contains an introductory script, app overview and course material in markdown format.

To convert the file, install Pandoc (https://pandoc.org/), version 2.0 or higher, and open a terminal window:
```
$ pandoc --lua-filter ./gitlab-math.lua latest.md -o latest.docx
```
Then, download and open "latest.docx" with Microsoft Word.

The markdown's latest version is 1.7.1. Known to work on Windows 10 Pro Version 1903, in Microsoft Word for Office 365 Version 1908 (64-bit)

## Usage

Instructors follow the introductory script and can keep the app overview for their personal reference.
Course material is distributed to students for them to complete. However, instructors should not simply hand them the material; they should illustrate some examples briefly.
On how to proceed from there is the instructor's discretion.

### Alternative Build Method

Install R (https://www.r-project.org/), as well; open a terminal window; then, use R to render the file as a Microsoft Word document:
```
$ R
$ install.packages("rmarkdown")
$ library(rmarkdown)
$ render("latest.md")
``` 
The benefit to rendering markdown with R is that one can also embed executable R code chunks (https://rmarkdown.rstudio.com/lesson-3.html). Embed a chunk; change the file's extension to .Rmd; then, re-render the file.

## Additional Resources

Jupyter/<p>
    
    Ten-Year_Minimum_Errors.ipynb 
    (for computing ten-year minimum monthly payment errors)

LaTeX/<p>

    deeper_insight.pdf
    (provides context, overview, terminology and formulae)

    extra_insight.pdf 
    (provides examples and derivations)

<!--deeper_insight.tex (source code)
    extra_insight.tex (source code)
    images/ (images for deeper_insight.pdf)
    images/svg/ (source of images for deeper_insight.pdf)-->

Other/<p>

    rounding_notes 
    (two notes about rounding quantities in Swift)

    checking_calculations.xlsx 
    (for checking app calculations)

    checklist_for_checking_calculations.docx 
    (checklist for checking app calculations)

## Contributing

Sign into GitLab, to fork the project.<p>

Modify any resources.<br>
Under Source Control, select Commit, and Push the changes.<p>

Return to GitLab, and submit a new pull request.<br>
For any issues, submit a new issue or discuss an existing one.<p>

## History

Sep 1-2, 2019 &middot; Version 1.7.1: merged resources from two repositories into one new repository, archived pdf files<br>
Aug 27, 2019 &middot; Version 1.7: updated interest rate and default numbers, aligned how savings and change in savings are calculated and displayed<br>
Aug 25, 2019 &middot; Version 1.6: updated handout<br>
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
