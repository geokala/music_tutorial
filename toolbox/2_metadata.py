notes = stream.Score()
notes.append(note.Note('c4'))
notes.append(note.Note('d4'))
notes.append(note.Note('e4'))
notes.append(note.Note('f4'))
tune = stream.Score(notes)

tune.metadata = metadata.Metadata(
    title='Toolbox 2, metadata',
    composer='Somebody',
)
