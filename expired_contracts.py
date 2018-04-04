from notification_manager import NotificationManager
from backend_service import BackendService

def main():
    nm = NotificationManager()
    bs = BackendService()
    
    ids = bs.expired_ids()
    email_to = bs.get_active_users()
    subject = 'kończące się umowy'
    body = nm.generate_body('notification', ids,
                            context={'subject': subject})

    # send mail to users
    nm.notify(subject, body, email_to)
    

if __name__ == '__main__':
    main()
