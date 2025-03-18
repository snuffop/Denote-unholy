# Denote-unholy

An Interpretation of Protesilaos Stavrou's Denote for shell and other than Emacs editors.

I'm Stealing much of the work from [Conan Theobald](https://github.com/shuckster/) to start this
project.  He has hard coded .md into the script, I will be enhancing that to
include  . org and .txt files.   

The file-name format:

```
20210319T202401--single-responsibility__software_solid_zettel.[md,org,txt]
^_____________^  ^___________________^  ^___________________^
      id                 title                   tags
```

I hope to add the "Optional" Signature section to the file names and front matter as well

```
20210319T202401==Signature--single-responsibility__software_solid_zettel.[md,org,txt]
^_____________^  ^_______^  ^___________________^  ^___________________^
      id            sig            title                   tags
```

The Markdown front-matter:

```md
---
identifier: "20210815T234244"
date: 2021-08-15T23:42:44.000Z
tags: [ "software", "javascript", "zettel" ]
title: "Currying"
signature: A1a
---
```

The links between notes:

```
Hop along to [[denote:20210815T234244]] for more info...
```
I Hope to add Multiple linking methods for Markdown including the above and 
```
Cruse over to [Title of the Note](denote:20210815T234244) for info
```


</details>

Once installed, configure these paths:

```sh
export DENOTE_MD_SCRIPT_PATH=/path/to/denote-md.sh
export DENOTE_MD_NOTES_PATH=/path/to/your/notes/folder/
```

---
Conan's Repos are [denote-md](https://github.com/shuckster/denote-md) and [vim-denote-mm](https://github.com/shuckster/vim-denote-md)

- Marty Buchaus


