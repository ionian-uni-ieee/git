# git exercise

Σκοπός αυτής της άσκησης είναι να κατανοήσετε το βάσικο Workflow του git σε συνδιασμό με το Github.
Καλείστε λοιπόν να τροποποιήσετε το αρχείο `org-status.py` έτσι ώστε κατά την εκτέλεση του, μαζί με το όνομα και
τον αριθμό των `forks`να εμφανίζεται και ο αριθμός τών `stars` του κάθε αποθετηρίου του
**IEEE Student Branch Of Ionian University**.

### Clone

Κάνε `clone` το `fork` σου γράφοντας:
  
  `git clone https://github.com/<your-username>/git`

### Execute

Αφού πλοηγηθείς στον σωστό φάκελο μπορείς να εκτελέσεις το πρόγραμμα γράφοντας:
  
  `python scripts/org-status.py`
  
### Create a new branch

Δημιούρησε ένα καινούργιο `branch` γράφοντας:
  
  `git branch <branch-name>`

Μπείτε στο branch γράφοντας:

  `git checkout <branch-name>`

### Add to stage

Αφού έχεις κάνει τις αλλαγές στο αρχείο πρόσθεσε το στο `stage` γράφοντας:

  `git add <file-name>`

### Commit

Επικύρωσε τις αλλαγές σου γράφοντας:

  `git commit -m '<commit-message>'`
  
### Push to remote

Κάνε `push` το καινούργιο σου `commit` γράφοντας:

  `git push -u <remote-name> <branch-name>`

### Pull Request

Τέλος άνοιξε ένα καινούργιο `Pull Request` στο `master branch` του αυθεντικού αποθετηρίου.

 
