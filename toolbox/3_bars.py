notes = stream.Score()

bar1 = stream.Measure()
bar1.append(note.Note('c4'))
bar1.append(note.Note('d4'))
bar1.append(note.Note('e4'))
bar1.append(note.Note('f4'))
notes.append(bar1)

bar2 = stream.Measure()
bar2.append(note.Note('g4'))
bar2.append(note.Note('a4'))
bar2.append(note.Note('b4'))
bar2.append(note.Note('c5'))
notes.append(bar2)

tune = stream.Score(notes)
