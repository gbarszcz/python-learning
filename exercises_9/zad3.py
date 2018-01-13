# coding=utf-8
# Napisz program który sprawdzi czy możliwe jest ustalenie spotkań
# użytkownika, tak żeby nie zazębiały się one między sobą. Program
# otrzymuje na wejściu informacje na temat ilości planowanych
# spotkań oraz ilość dni w terminarzu a następnie informacje na
# temat spotkań w postaci początek spotkania, koniec spotkania,
# dzien spotkania. Program ma zwrócić m wierszy z informacją TAK
# lub NIE w zależności czy da się ustalić spotkania danego dnia.
# Jeżeli odpowiedź to tak, program ma wypisać dwa numery
# pasujących spotkań. W ciągu jednego dnia użytkownik może mieć
# maksymalnie dwa spotkania.
# Napisz testy jednostkowe weryfikujące poprawność rozwiązania.


class Meeting:
    id = None
    begin = None
    end = None
    day = None

    def __init__(self, i, d, b, e):
        self.id = i + 1
        self.day = d
        self.begin = b
        self.end = e


def date_between(v, date):
    return v.begin < date < v.end


class Schedule:
    schedule = None

    def __init__(self):
        self.schedule = {}

    def add(self, m):
        self.schedule[m.day].append(m)

    def meetings_not_exclusive(self, m, meeting):
        if m.begin <= meeting.begin <= m.end or m.begin <= meeting.end <= m.end:
            return False
        elif m.begin >= meeting.begin and m.end <= meeting.end:
            return False
        elif meeting.begin >= m.begin and meeting.end <= m.end:
            return False
        return True

    def is_available(self, m):
        if self.schedule.get(m.day) is None:
            self.schedule[m.day] = []
            return True
        meetings = self.schedule[m.day]
        for meeting in meetings:
            return self.meetings_not_exclusive(m, meeting)
        return True


def initSchedule():
    meetings_count = input("Meetings count: ")
    days_count = input("Days count in a schedula: ")

    schedule = Schedule()

    for i in range(0, meetings_count):
        meeting_begin = input("Begin: ")
        meeting_end = input("End: ")
        meeting_day = input("Day: ")
        meeting = Meeting(i, meeting_day, meeting_begin, meeting_end)
        # if schedule.schedule.get(meeting_day) is not None and len(schedule.schedule[meeting_day]) == 2:
        #     print "You already have 2 appointments on day " + str(meeting_day) + ".\n"
        if schedule.is_available(meeting):
            schedule.add(meeting)

    # for i in range(1, meetings_count):
    for key, values in schedule.schedule.iteritems():
        if len(values) == 2:
            output = "TAK "
            for value in values:
                output = output + str(value.id) + " "
            print output
        else:
            print "NIE"


input = input()
initSchedule()
