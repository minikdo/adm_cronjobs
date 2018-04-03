from notification_manager import NotificationManager


def main():
    nm = NotificationManager()

    ids = nm.get_ids("wyl < now()")
    template = 'expired'
    subject = 'umowy zakończone'
    
    nm.notify(template, subject, ids)
    

if __name__ == '__main__':
    main()



