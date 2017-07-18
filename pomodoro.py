from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

# get task and sessions required and pass it to the clock


def task_n_session():
    task = input('Please enter a task: ')
    session = input('Please enter the number of sessions you need: ')
    toaster.show_toast("Pomodoro Clock started!!",
                       "Let's do it :)")
    pomodoro_clock(task, session)

# creating the pomodoro clock


def pomodoro_clock(task, session):

    session_value = int(session)

    # for 3 or lesser the break time will be 5 minutes only
    if session_value < 4:

        for i in range(session_value):
            time.sleep(1200)
            toaster.show_toast("Pomodoro Notifications!!",
                               "Break time :)")
            time.sleep(300)
            toaster.show_toast("Pomodoro Notifications!!",
                               "Back to work xD")

        # if user needs more sessions for completion
        more_sessions = input('Hey do you need more sessions ? [y/n] : ')

        if more_sessions == 'y':
            task_n_session()
        else:
            print('Congrats! You did a great Job :)')

    # for every fourth clock the break time will be 20 minutes
    else:
        j = 1
        for i in range(session_value):
            if j % 4 != 0:
                time.sleep(1200)
                toaster.show_toast("Pomodoro Notifications!!",
                                   "Break time :)")
                time.sleep(300)
                toaster.show_toast("Pomodoro Notifications!!",
                                   "Back to work xD")
            else:
                time.sleep(1200)
                toaster.show_toast("Pomodoro Notifications!!",
                                   "Take 20min Break time :)")
                time.sleep(1200)
                toaster.show_toast("Pomodoro Notifications!!",
                                   "Back to work xD")
            j += 1

        # if user needs more sessions for completion
        more_sessions = input('Hey do you need more sessions ? [y/n] : ')

        if more_sessions == 'y':
            task_n_session()
        else:
            print('Congrats! You did a great Job :)')


task_n_session()
