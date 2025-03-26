on run argv
    set pdfPath to POSIX file (item 1 of argv) as alias
    set the clipboard to ""
    tell application "Preview"
        activate
        open pdfPath
        delay 2
        tell application "System Events"
            keystroke "a" using command down
            delay 1
            keystroke "c" using command down
            delay 1
        end tell
        close front window
    end tell
    delay 1
    try
        return (the clipboard as text)
    on error
        return ""
    end try
end run
