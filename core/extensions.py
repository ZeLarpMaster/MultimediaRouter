EXTENSIONS = {
    "Text": [
        ".doc", ".docx", ".log", ".msg", ".odt", ".pages", ".rtf", ".tex", ".txt", ".wpd", ".wps"
    ],
    "Data": [
        ".csv", ".dat", ".ged", ".key", ".keychain", ".pps", ".ppt", ".pptx", ".sdf", ".tar", ".tax2016",
        ".tax2017", ".vcf", ".xml"
    ],
    "Audio": [
        ".aif", ".iff", ".m3u", ".m4a", ".mid", ".mp3", ".mpa", ".wav", ".wma"
    ],
    "Video": [
        ".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".srt", ".swf",
        ".vob", ".wmv"
    ],
    "3D Image": [
        ".3dm", ".3ds", ".max", ".obj"
    ],
    "Raster Image": [
        ".bmp", ".dds", ".gif", ".jpg", ".png", ".psd", ".pspimage", ".tga", ".thm", ".tif",
        ".tiff", ".yuv"
    ],
    "Vector Image": [
        ".ai", ".eps", ".ps", ".svg"
    ],
    "Page Layout": [
        ".indd", ".pct", ".pdf"
    ],
    "Spreadsheet": [
        ".xlr", ".xls", ".xlsx"
    ],
    "Database": [
        ".accdb", ".db", ".dbf", ".mdb", ".pdb", ".sql"
    ],
    "Executable": [
        ".apk", ".app", ".bat", ".cgi", ".com", ".exe", ".gadget", ".jar", ".wsf"
    ],
    "Game": [
        ".dem", ".gam", ".nes", ".rom", ".sav"
    ],
    "CAD": [
        ".dwg", ".dxf"
    ],
    "GIS": [
        ".gpx", ".kml", ".kmz"
    ],
    "Web": [
        ".asp", ".aspx", ".cer", ".cfm", ".csr", ".css", ".htm", ".html", ".js", ".jsp", ".php", ".rss",
        ".xhtml"
    ],
    "Plugin": [
        ".crx", ".plugin"
    ],
    "Font": [
        ".fnt", ".fon", ".otf", ".ttf"
    ],
    "System": [
        ".cab", ".cpl", ".cur", ".deskthemepack", ".dll", ".dmp", ".drv", ".icns", ".ico", ".lnk",
        ".sys"
    ],
    "Settings": [
        ".cfg", ".ini", ".prf"
    ],
    "Encoded": [
        ".hqx", ".mim", ".uue"
    ],
    "Compressed": [
        ".7z", ".cbr", ".deb", ".gz", ".pkg", ".rar", ".rpm", ".sitx", ".tar.gz", ".zip", ".zipx"
    ],
    "Disk Image": [
        ".bin", ".cue", ".dmg", ".iso", ".mdf", ".toast", ".vcd"
    ],
    "Developer": [
        ".c", ".class", ".cpp", ".cs", ".dtd", ".fla", ".h", ".java", ".lua", ".m", ".pl", ".py",
        ".sh", ".sln", ".swift", ".vb", ".vcxproj", ".xcodeproj"
    ],
    "Backup": [
        ".bak", ".tmp"
    ],
    "Misc": [
        ".crdownload", ".ics", ".msi", ".part", ".torrent"
    ]
}

CATEGORIES = {v: k for k, vs in EXTENSIONS.items() for v in vs}

__all__ = ["EXTENSIONS", "CATEGORIES"]
