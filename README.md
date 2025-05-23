# Χρονοσειρά Εγγραφών Χρηστών (Django + HTMX + Alpine.js)

## Περιγραφή

Η εφαρμογή προβάλει καθημερινές εγγραφές χρηστών, παρέχοντας:

- Πίνακα και γραφική παράσταση εγγραφών ανά ημερομηνία
- Δυνατότητα φιλτραρίσματος με βάση εύρος ημερομηνιών
- Δυναμική ενημέρωση με HTMX χωρίς επαναφόρτωση σελίδας
- Ελαφριά διαχείριση εμφάνισης με Alpine.js

---

## Οδηγίες Εγκατάστασης

1. Δημιουργία και ενεργοποίηση εικονικού περιβάλλοντος:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows

2. Εγκατάσταση εξαρτήσεων: `pip install -r requirements.txt`

3. Δημιουργία βάσης δεδομένων: `python manage.py migrate`

4. Δημιουργία χρηστών για δοκιμές: `python manage.py create_users`

5. Εκκίνηση τοπικού server: `python manage.py runserver`

6. Πρόσβαση στην εφαρμογή:

Frontend: http://127.0.0.1:8000/

API (JSON): http://127.0.0.1:8000/stats/

## Δεδομένα Δοκιμής

Η εντολή: `python manage.py create_users`

δημιουργεί 100 τυχαίους χρήστες με date_joined τιμές εντός των τελευταίων 30 ημερών.

## Υποθέσεις

Χρησιμοποιείται custom user model (CustomUser με βάση το AbstractUser)

Το backend API επιστρέφει JSON εγγραφών ανά ημέρα

Όλος ο κώδικας ακολουθεί τις βέλτιστες πρακτικές του Django (apps, templates, urls)

## Δομή Φακέλων (ενδεικτικά)

userstats/
├── dashboard/
│   ├── templates/dashboard/user_stats.html
│   ├── management/commands/create_users.py
│   ├── views.py
│   ├── urls.py
│   ├── models.py
├── userstats/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py


## Σας ευχαριστώ για την ευκαιρία να συμμετάσχω σε αυτή τη φάση της συνέντευξης


