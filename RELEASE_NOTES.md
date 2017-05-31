#### 31.05.2017
#### web_kanban_gauge, 1.0.2
##### CHG
- Anpassung der Anzeige des Gauge-Widgets z.B. 2k -> 2000

#### 29.05.2017
#### sale, 1.3.7
##### CHG/FIX
- Ticket #4252: Bei prozentualer Abrechnung wird jetzt eine Umsatzsteuer für die prozentuale Anzahlung erzeugt. (FIX aus https://github.com/odoo/odoo/pull/6073/commits/2ba5e58b6fafa24ffffb233057824074f79f1515)

#### 23.05.2017
#### mrp, 1.1.15
##### CHG
- Übersetzung geändert: Im Arbeitsplan "Tätigkeit" zu "Arbeitsplan" geändert.

#### 20.04.2017
#### mrp, 1.1.14
##### CHG
- Feld "code" auf size = 64 geändert (vorher 8)

#### 11.04.2017
#### product, 1.1.9
##### CHG
- Übersetzung angepasst "Mininale Menge" in "Mindestbestellmenge"

#### 04.04.2017
#### mrp, 1.1.13
##### CHG
- Übersetzung angepasst

#### 04.04.2017
#### mrp_operations, 1.0.4
##### CHG
- Übersetzung angepasst

#### 03.04.2017
#### mrp_operations, 1.0.3
##### CHG
- Feld 'date_planned_end' als store=True definiert. 

#### 28.03.2017
#### mrp, 1.1.12
##### CHG
- Übersetzungen  "Anzahl Zyklen" in "Anzahl Teile".

#### 28.03.2017
#### mrp, 1.1.11
##### CHG
- Übersetzungen angepasst.

#### 28.03.2017
#### mrp_operations, 1.1.2
##### CHG
- Übersetzung angepasst + Feld "Zwingende Abfolge" auf unsichtbar gesetzt.

#### 27.03.2017
#### mrp, 1.1.10
##### CHG
- Menüpunkt "Stückliste Komponenten" wurde entfernt (auskommentiert).

#### 27.03.2017
#### mrp, 1.1.9
##### CHG
- Anpassung Übersetzungen.

#### 16.03.2017
#### mrp, 1.1.8
##### CHG
- Feld "Referenz" (code) auf size=64 (vorher 16) geändert.

#### 18.08.2016
#### mail, 1.0.7
##### CHG
- Anpassungen für die Verarbeitung eingehender E-Mails

#### 07.02.2017
#### web, 1.10.3
##### FIX
- Die Einrückung der BoM - Treeview war nicht korrekt.   

#### 15.12.2016
#### mrp, 1.1.5
##### ADD/CHG
- In der Form-Ansicht eines Fertigungauftrags wurde zwischen Produktmenge und Produkteinheit ein margin-left 5px eingefügt.
- Übersetzung "Anfangsdatum" zu "Startdatum" geändert.

#### 23.11.2016
#### mrp, 1.1.3
##### CHG
- Feld "workcenter_lines" wird jetzt nicht mehr Über Python Code als readonly definiert. Jetzt werden die einzelnen Felder der "workcenter_lines" in der View als readonly definiert, dies ermöglicht eine nachträgliche Bearbeitung der readonly Funktion (z.B vorhandene View überschreiben und readonly auf false setzen).

#### 22.11.2016
#### mass_mailing, 2.3.4
##### FIX
- Korrektur in Referenzierung der Basisfunktion "_" für dyn. Lokalisierung aus dem SourceCode

#### 21.11.2016
#### crm, 1.4.6
##### CHG
- Template "Lead/Opportunity Mass Mail" in ein noupdate = "0" eingefügt.

#### 21.11.2016
#### crm, 1.4.5
##### CHG
- forcecreate bei dem Template "Lead/Opportunity Mass Mail" entfernt, dieses Template wird nicht via Equitania-Skript eingefügt.

#### 14.11.2016
#### hr, 1.1.3
##### CHG
- Typecast der Felder expected_employees und no_of_employee auf Float, da die Datenbank ein Numeric erwartet. Diese Änderung bereinigt folgende Warning:WARNING basis_skr03 openerp.models.schema: Table hr_job: column has changed type (DB=numeric, def=integer), data moved to column `expected_employees_moved10` etc.

#### 14.11.2016
#### web, 1.10.2
##### CHG
- maximale Größe eines Uploads auf 50 MB erhöht.

#### 10.11.2016
#### website_sale_delivery, 1.1.2
##### FIX
- Korrektur der Übersetzung

#### 10.11.2016
#### website, 1.1.1
#### RELEASE NOTES
>>>>>>> branch 'develop' of git@github.com:equitania/myodoo-server.git
##### CHG
- Release notes bearbeitet: Modul website entfernt, da es eine eigene Release note bekommen hat.

#### 02.11.2016
#### portal, 1.0.2
##### CHG
- automatischen Link in Email-Templates zum Partner entfernt

#### 26.10.2016
#### website_quote, 1.1.2
##### CHG
- Feld im Template "Angebot gültig bis" entfernt, da wir das an dieser Stelle nirgendwo im Einsatz haben

#### 18.10.2016
#### payment_tranfer, 1.0.1
##### CHG
- Deutsche Übersetzung angepasst


#### 29.09.2016
#### web, 1.0.8
##### CHG
- Abfrage hinzugefügt, welche eine Autokorrektur des Editors verhindert sobald eine Schleife sich im Text befindet.


#### 20.09.2016
#### web, 1.0.7
##### CHG
- In der JavaScript-Datei jquery.cleditor.js Zeile 1177-1180 wieder einkomentiert, sodass eine Bearbeitung von multilingualen Texten (Kopf- und Fußtexten) wieder möglich ist.

#### 18.08.2016
#### mail, 1.0.3
##### CHG
- Änderung der Übersetzung von "Empfänger" zu "Zugeordneter Partner".

#### 16.08.2016
#### mail, 1.0.2
##### CHG
- Kontext vom Posteingang auskommentiert. Dieser hat die Anzeige von zugeordneten mail.messages blockiert.


#### 15.07.2016
#### product, 1.1.3
##### CHG
- Anpassungen für Setzen des Preises


#### 13.07.2016
#### account_followup, 1.0.3
##### IMP
- Übersetzungsdatei, und passende Texte angepasst


#### 11.07.2016
#### account_followup, 1.0.2
##### FIX
- de.po Datei korrigiert, sodass beim Aufruf des Parameters partner_name dieser auch als String angesehen wird (Beispiel: %(partner_name)s ). Das "s" fehlte in der kompletten de.po Datei nach dem Aufruf des jeweiligen Parameters.


#### 29.06.2016
#### point_of_sale, 1.0.3
##### FIX
- Tippfehler in der Versionsnummer korrigiert, damit man Odoo wieder starten kann


#### 29.06.2016
#### account, 1.1.4
##### CHG
- Das Feld attachment bei dem Bericht "Rechnungen" wird nun nicht mehr gesetzt (auskommentiert).


#### 20.06.2016
#### account_analytic_analysis, 1.2
##### ADD
- Noupdate="1" und forcecreate="False" beim Email Template "Contract expiration reminder" eingefügt, sodass das Template nach einem Löschvorgang auch gelöscht bleibt.

#### 20.06.2016
#### calendar, 1.4
##### CHG
- Übersetzung der Email-Templates zu "Meeting Invitation", "Meeting Invitation - Reminder" und "Meeting Invitation - Change Date" aus der .po-Datei entfernt. Dadurch wird die Übersetzung nicht mehr über die importierten Template geladen.

#### 20.06.2016
#### crm, 1.4
##### CHG
- Übersetzung des Email-Templates zu "Reminder to User" aus der .po-Datei entfernt. Dadurch wird die Übersetzung nicht mehr über das importierte Template geladen.

#### 20.06.2016
#### auth_signup, 1.0.5
##### CHG
- Übersetzung des Email-Templates zu "Password Reset" aus der .po-Datei entfernt. Dadurch wird die Übersetzung nicht mehr über das importierte Template geladen.

#### 20.06.2016
#### purchase, 1.4
##### CHG
- Übersetzung der Email-Templates zu "RFQ - Send by Email" und "Purchase Order - Send by Email" aus der .po-Datei entfernt. Dadurch wird die Übersetzung nicht mehr über das importierte Template geladen.

#### 20.06.2016
#### account, 1.1.3
##### CHG
- Übersetzung des Email-Templates zu "Invoice - Send by Email" aus der .po-Datei entfernt. Dadurch wird die Übersetzung nicht mehr über das importierte Template geladen.

#### 20.06.2016
#### sale, 1.3
##### CHG
- Übersetzung des Email-Templates zu "Sales Order - Send by Email" aus der .po-Datei entfernt. Dadurch wird die Übersetzung nicht mehr über das importierte Template geladen.

#### 16.06.2016
#### calendar, 1.3
##### ADD
- Deutsche Übersetzung für at...To (von...bis) für das Email-Template "Meeting Invitation - Change Date" hinzugefügt.

#### 03.06.2016
#### web, 1.0.19
##### CHG
- Änderung in Generierung von Meta-Tag "Robots" auf den Seiten. Der Wert wird ab jetzt aus der Tabelle ir_ui_view.website_meta_robots geholt

#### 01.06.2016
#### web, 1.0.4
##### FIX
- Die JavaScript-Datei jquery.cleditor.js dementsprechend angepasst, sodass keine Autovervollständigung mehr stattfindet.

#### 31.05.2016
#### web, 1.0.3
##### FIX
- JavaScript debugger entfernt.

#### 31.05.2016
#### web, 1.0.2
##### CHG
- JavaScript Datei "view_form.js" so angepasst (Aufruf der Funktion "updateTextArea()" auskommentiert), dass bei einer Bearbeitung der Email-Templates im ersten Editor keine Auto-Verollständigung mehr stattfindet.

#### 31.05.2016
#### web_analytics, 1.0.1
##### ADD
- Übersetzungsdatei de.po in Ordner i18n eingefügt

#### email_template, 1.4
##### CHG
- Bei dem Email-Template zu Partner Mass Mail musste um das dauerhafte Löschen zu gewährleisten noch ein noupdate="1" eingefügt werden. Außerdem wurde die entsprechende Action act_window zu dem Template auskommentiert, um bei einem Löschen des Templates eine fehlende Referenzierung zu verhindern.

#### 31.05.2016
#### auth_signup, 1.0.4
##### CHG
- Bei dem Email-Template zu Reset Password und Odoo Enterprise Connection musste um das dauerhafte Löschen zu gewährleisten noch ein noupdate="1" eingefügt werden.

#### 31.05.2016
#### crm_partner_assign, 1.2
##### CHG
- Bei dem Email-Template zu Lead Mass Mail musste um das dauerhafte Löschen zu gewährleisten noch ein noupdate="1" eingefügt werden.

#### 31.05.2016
#### crm, 1.3
##### CHG
- Action act_window zu dem Template "Lead/Opportunity Mass Mail" auskommentiert, um bei einem Löschen des Templates eine fehlende Referenzierung zu verhindern.

#### 30.05.2016
#### purchase, 1.3
##### CHG
- Bei dem Email-Template zu RFQ - Send by Email ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### auth_signup, 1.0.3
##### CHG
- Bei dem Email-Template zu Reset Password ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### crm, 1.2
##### CHG
- Bei dem Email-Template zu Reminder to User ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### purchase, 1.2
##### CHG
- Bei dem Email-Template zu Purchase Order - Send by Email ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### email_template, 1.3
##### CHG
- Bei dem Email-Template zu Partner Mass Mail ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### auth_signup, 1.0.2
##### CHG
- Bei dem Email-Template zu Odoo Enterprise Connection ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### calendar, 1.2
##### CHG
- Bei den 3 Email-Templates zu Meeting Invitation ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### crm, 1.1
##### CHG
- Bei dem Email-Template zu Lead/Opportunity Mass Mail ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### crm_partner_assign, 1.1
##### CHG
- Bei dem Email-Template zu Lead Mass Mail ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### portal_sale, 0.3
##### CHG
- Bei dem Email-Template zu Invoice - Send by Email (Portal) ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### account, 1.1.2
##### CHG
- Bei dem Email-Template zu Invoice - Send by Email ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### website_quote, 1.1
##### Fix
- Bei dem Email-Template zu Sales Order - Send by Email (Online Quote) ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### sale, 1.2
##### Fix
- Copy-Paste-Fehler entfernt.

#### 30.05.2016
#### sale, 1.1
##### CHG
- Bei dem Email-Template zu Sales Order - Send by Email ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 30.05.2016
#### portal_sale, 0.2
##### CHG
- Bei dem Email-Template zu Sales Order - Send by Email (Portal) ein forcecreate="False" eingefügt. Dadurch bleibt bei einem Löschen des Templates das Template gelöscht.

#### 19.05.2016
#### mass_mailing, 2.3
##### ADD
- Für die Weiterleitung bei dem Link "Newsletter abbestellen" wird jetzt das Layout der Webseite gerendert. Außerdem wurde eine Ansicht geschaffen, die jetzt vom Aussehen und von der Formatierung angepasst werden kann.

#### 19.05.2016
#### web, 1.0.1
##### FIX
- Korrektur für das Problem mit dem Button "Speichern", der im Editmodus nicht aktiviert wurde

#### 02.05.2016
#### auth_signup, 1.0.1
##### Änderung
- E-Mail Template Passwort-Zurücksetzen Fomratierungsfehler entfernt.

#### 19.04.2016
#### website_sale_options, 1.0.1
##### FIX
- Übersetzung "Produkt zum verschieben in Einkaufskorb" mit "Produkt zum Warenkorb hinzufügen" ersetzt