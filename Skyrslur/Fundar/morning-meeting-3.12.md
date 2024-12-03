#########  Day-1 - 25/11/24 ############################

Mættir / In attendance: 
    Hreimur
    Daniela
    Jon
    Kormakur
    Tumi
    Yeabsira

Málefni rædd / Issues addressed: 
    1) Talked about what we are going to to for the day
    Hreimur is working on making dummy data for our json
    Daniela og Kormakur working on UI
    Jon and Yeabsira working on the storage layer
    and Tumi working on the wrappers

    2) Issues regarding writing to file - Risk of dataloss.
    Desc: We realised that changing (writing) files could 
    result in total loss of a data if case of power loss.
    The problem is that we change the file by overwriting
    the existing datafile.
    Chuck proposed to save to a temp file the changed data
    and then delete the old file and rename the temp file.
    This way there is no chance to losing data. 

Dagskrá fyrir næsta fund / Agenda for next meeting: 

Chuck is going to re-write how our system writes / updates 
       files using temp files.
Gylfi will be busy grading TOLH but will take on tasks
from the "todo-list" if he becomes available before the
next meeting. 
Next meeting is scheduled for Thursday 26th. at 11:30.

Forgangsraðaður listi / Priority ToDo-list of outstanding tasks:
    Priority 1: 

Fix the issue with writing to files (see above)
Make the UI wire frame for use cases 11 to 15 (new / edit staff)
Priority 2: 
Write text with the Model Classes diagram in the report.
Send a reminder to the Pope for next meeting (hope he shows)

######### End of entry for day-1 - 25/11/24 ############################