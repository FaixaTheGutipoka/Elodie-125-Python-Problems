def ryerson_letter_grade(pct):
    if 100>=pct>=90:
        a='A+'
    elif 89>=pct>=85:
        a='A'
    elif 84>=pct>=80:
        a='A-'
    elif 79>=pct>=77:
        a='B+'
    elif 76>=pct>=73:
        a='B'
    elif 72>=pct>=70:
        a='B-'
    elif 69>=pct>=67:
        a='C+'
    elif 66>=pct>=63:
        a='C'
    elif 62>=pct>=60:
        a='C-'
    elif 59>=pct>=57:
        a='D+'
    elif 56>=pct>=53:
        a='D'
    elif 52>=pct>=50:
        a='D-'
    else:
        a='F'

    return a

print(ryerson_letter_grade(34))
