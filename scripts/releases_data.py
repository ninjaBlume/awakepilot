"""Release notes shown on the website (EN / DE / TR).

Add a new release at the TOP of RELEASES, then run `python3 scripts/build_releases.py`.
Text may use `code` and **bold** inline.
"""

LANGS = {
    "en": {
        "dir": "docs", "locale": "en_US", "prefix": "", "date_fmt": "{month} {day}, {year}",
        "months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "title": "Release notes — Awakepilot",
        "description": "Every Awakepilot release, from the first production build to today.",
        "kicker": "Release notes",
        "h1": "What’s new in Awakepilot.",
        "lead": "Every release, from the first production build to today. Packages are signed with a Developer ID certificate and notarized by Apple, and Awakepilot checks for new versions automatically.",
        "download": "Download for Mac", "support": "Support", "support_href": "support.html",
        "latest": "Latest", "index_label": "Versions",
    },
    "de": {
        "dir": "docs/de", "locale": "de_DE", "prefix": "de/", "date_fmt": "{day}. {month} {year}",
        "months": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
        "title": "Versionshinweise — Awakepilot",
        "description": "Alle Awakepilot-Versionen, vom ersten produktiven Build bis heute.",
        "kicker": "Versionshinweise",
        "h1": "Neues in Awakepilot.",
        "lead": "Jede Version, vom ersten produktiven Build bis heute. Pakete sind mit einem Developer-ID-Zertifikat signiert und von Apple notarisiert; Awakepilot sucht automatisch nach neuen Versionen.",
        "download": "Für Mac laden", "support": "Support", "support_href": "support.html",
        "latest": "Aktuell", "index_label": "Versionen",
    },
    "tr": {
        "dir": "docs/tr", "locale": "tr_TR", "prefix": "tr/", "date_fmt": "{day} {month} {year}",
        "months": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"],
        "title": "Sürüm notları — Awakepilot",
        "description": "Awakepilot’un ilk üretim sürümünden bugüne tüm sürümleri.",
        "kicker": "Sürüm notları",
        "h1": "Awakepilot’ta yeni olanlar.",
        "lead": "İlk üretim sürümünden bugüne her sürüm. Paketler Developer ID sertifikasıyla imzalanır ve Apple tarafından onaylanır; Awakepilot yeni sürümleri kendiliğinden denetler.",
        "download": "Mac için indir", "support": "Destek", "support_href": "support.html",
        "latest": "Güncel", "index_label": "Sürümler",
    },
}

# Each release: version, ISO date, and per-language summary / sections / optional note.
# A section is (heading, [bullets]) or (heading, "paragraph").
RELEASES = [
    {
        "version": "0.14.1", "date": (2026, 10, 1),
        "en": {
            "summary": "Reliable in-app updates and clearer controls.",
            "sections": [
                ("Reliable updates", [
                    "Fixed installation getting stuck when the About and Updates sheet prevented the app from quitting. The sheet now closes before installation hands over to the updater.",
                    "If quitting is cancelled, an actionable error appears after five seconds. The installer helper also stops waiting after 30 seconds instead of waiting indefinitely.",
                    "Automatic checks now run every 24 hours while the app remains open, with a due check after wake. Failed automatic checks retry after an hour; manual checks remain available.",
                    "Running jobs continue to block installation, including jobs started while an update is being prepared.",
                ]),
                ("Clearer controls and help", [
                    "Revised interface text in English, German, Spanish, French, Azerbaijani, and Turkish, including explanations of screen behavior, activity thresholds, automation matching, and time limits.",
                    "Improved wrapping for longer settings descriptions.",
                    "Updated the English, German, and Turkish website, support pages, and screenshots.",
                ]),
            ],
            "note": ("Updating from 0.14.0 or earlier",
                     "This first update still uses the updater in your installed version. If **Installing update** remains visible for more than a minute, close **About and Updates**, then quit Awakepilot from the menu bar menu. The prepared update can then finish and relaunch the app. If it does not, install the latest official DMG with the Download button. The installation fix takes effect once 0.14.1 is installed."),
        },
        "de": {
            "summary": "Zuverlässige Updates in der App und klarere Einstellungen.",
            "sections": [
                ("Zuverlässige Updates", [
                    "Die Installation hängt nicht mehr, wenn das Fenster „Über und Updates“ das Beenden der App verhinderte. Das Fenster wird jetzt geschlossen, bevor die Installation an den Updater übergeben wird.",
                    "Wird das Beenden abgebrochen, erscheint nach fünf Sekunden eine verständliche Fehlermeldung. Der Installationshelfer wartet außerdem höchstens 30 Sekunden, statt unbegrenzt zu warten.",
                    "Automatische Prüfungen laufen jetzt alle 24 Stunden, solange die App geöffnet bleibt, und holen nach dem Aufwachen eine fällige Prüfung nach. Fehlgeschlagene automatische Prüfungen werden nach einer Stunde wiederholt; manuelle Prüfungen bleiben jederzeit möglich.",
                    "Laufende Aufgaben verhindern weiterhin die Installation, auch solche, die gestartet werden, während ein Update vorbereitet wird.",
                ]),
                ("Klarere Einstellungen und Hilfe", [
                    "Überarbeitete Oberflächentexte in Englisch, Deutsch, Spanisch, Französisch, Aserbaidschanisch und Türkisch, einschließlich Erklärungen zu Bildschirmverhalten, Aktivitätsschwellen, Automatisierungsabgleich und Zeitlimits.",
                    "Besserer Umbruch bei längeren Beschreibungen in den Einstellungen.",
                    "Englische, deutsche und türkische Website, Support-Seiten und Screenshots aktualisiert.",
                ]),
            ],
            "note": ("Update von 0.14.0 oder früher",
                     "Dieses erste Update nutzt noch den Updater der installierten Version. Bleibt **Update wird installiert** länger als eine Minute sichtbar, schließe **Über und Updates** und beende Awakepilot über das Menü in der Menüleiste. Das vorbereitete Update kann dann abgeschlossen werden und startet die App neu. Falls nicht, installiere das aktuelle offizielle DMG über die Schaltfläche „Herunterladen“. Die Korrektur der Installation greift, sobald 0.14.1 installiert ist."),
        },
        "tr": {
            "summary": "Uygulama içinde güvenilir güncellemeler ve daha net denetimler.",
            "sections": [
                ("Güvenilir güncellemeler", [
                    "Hakkında ve Güncellemeler penceresi uygulamanın kapanmasını engellediğinde kurulumun takılı kalması düzeltildi. Pencere artık kurulum güncelleyiciye devredilmeden önce kapanıyor.",
                    "Kapatma iptal edilirse beş saniye sonra ne yapılacağını anlatan bir hata görünür. Kurulum yardımcısı da süresiz beklemek yerine 30 saniye sonra beklemeyi bırakır.",
                    "Otomatik denetimler uygulama açık kaldığı sürece 24 saatte bir çalışır; uyku sonrasında vakti gelmiş denetim yapılır. Başarısız otomatik denetimler bir saat sonra yeniden denenir; elle denetim her zaman kullanılabilir.",
                    "Çalışan işler kurulumu engellemeyi sürdürür; güncelleme hazırlanırken başlatılanlar da buna dahildir.",
                ]),
                ("Daha net denetimler ve yardım", [
                    "Arayüz metinleri İngilizce, Almanca, İspanyolca, Fransızca, Azerice ve Türkçe için gözden geçirildi; ekran davranışı, etkinlik eşikleri, otomasyon eşleştirme ve zaman sınırları açıklamaları dahil.",
                    "Uzun ayar açıklamalarında satır kaydırma iyileştirildi.",
                    "İngilizce, Almanca ve Türkçe web sitesi, destek sayfaları ve ekran görüntüleri güncellendi.",
                ]),
            ],
            "note": ("0.14.0 veya öncesinden güncelleme",
                     "Bu ilk güncelleme hâlâ yüklü sürümünüzdeki güncelleyiciyi kullanır. **Güncelleme yükleniyor** ifadesi bir dakikadan uzun görünür kalırsa **Hakkında ve Güncellemeler** penceresini kapatın, ardından Awakepilot’tan menü çubuğu menüsünden çıkın. Hazırlanan güncelleme tamamlanır ve uygulama yeniden açılır. Açılmazsa İndir düğmesindeki güncel resmî DMG’yi kurun. Kurulum düzeltmesi 0.14.1 yüklendikten sonra geçerli olur."),
        },
    },
    {
        "version": "0.14.0", "date": (2026, 10, 1),
        "en": {
            "summary": "Extends work-aware automation to connected hardware, audio routes, and the active network configuration.",
            "sections": [
                ("Highlights", [
                    "Start automation when a selected USB device is connected.",
                    "Follow selected paired Bluetooth devices as they connect and disconnect.",
                    "Keep a session active while a selected macOS audio output is the current route.",
                    "Match selected DNS server addresses from the active resolver configuration.",
                    "Match exact IPv4 or IPv6 addresses and CIDR networks.",
                    "Assign an independent session profile, display policy, and maximum duration to each new condition type.",
                    "Save the new hardware and network-context rules inside reusable workflow profiles.",
                    "Add complete English, German, Spanish, French, Azerbaijani, and Turkish interface coverage.",
                    "Open the disk image with large drag-to-install icons, a directional arrow, and a Retina background.",
                ]),
                ("Privacy and permissions",
                 "USB and audio-output detection use local macOS system APIs. Bluetooth rules inspect only connected paired-device identity and require the standard macOS Bluetooth permission. Device names, DNS server addresses, and IP rules remain in the current macOS user account. Diagnostic reports include only rule counts and enabled states; they exclude configured device names, DNS servers, IP rules, and activity history."),
            ],
        },
        "de": {
            "summary": "Erweitert die arbeitsbewusste Automatisierung auf angeschlossene Hardware, Audio-Ausgaben und die aktive Netzwerkkonfiguration.",
            "sections": [
                ("Highlights", [
                    "Starte die Automatisierung, wenn ein ausgewähltes USB-Gerät verbunden wird.",
                    "Folge ausgewählten gekoppelten Bluetooth-Geräten beim Verbinden und Trennen.",
                    "Halte eine Sitzung aktiv, solange ein ausgewählter macOS-Audioausgang die aktuelle Route ist.",
                    "Gleiche ausgewählte DNS-Serveradressen der aktiven Resolver-Konfiguration ab.",
                    "Gleiche exakte IPv4- oder IPv6-Adressen und CIDR-Netzwerke ab.",
                    "Weise jedem neuen Bedingungstyp ein eigenes Sitzungsprofil, eine eigene Bildschirmrichtlinie und eine eigene Höchstdauer zu.",
                    "Speichere die neuen Hardware- und Netzwerkkontext-Regeln in wiederverwendbaren Workflow-Profilen.",
                    "Vollständige Oberflächenabdeckung in Englisch, Deutsch, Spanisch, Französisch, Aserbaidschanisch und Türkisch.",
                    "Das Festplattenabbild öffnet sich jetzt mit großen Drag-to-install-Symbolen, einem Richtungspfeil und einem Retina-Hintergrund.",
                ]),
                ("Datenschutz und Berechtigungen",
                 "Die Erkennung von USB und Audioausgängen nutzt lokale macOS-System-APIs. Bluetooth-Regeln prüfen nur die Identität verbundener gekoppelter Geräte und benötigen die übliche macOS-Bluetooth-Berechtigung. Gerätenamen, DNS-Serveradressen und IP-Regeln bleiben im aktuellen macOS-Benutzerkonto. Diagnoseberichte enthalten nur die Anzahl und den Aktivierungsstatus der Regeln; konfigurierte Gerätenamen, DNS-Server, IP-Regeln und der Aktivitätsverlauf sind ausgeschlossen."),
            ],
        },
        "tr": {
            "summary": "İş farkındalıklı otomasyonu bağlı donanımlara, ses çıkışlarına ve etkin ağ yapılandırmasına genişletir.",
            "sections": [
                ("Öne çıkanlar", [
                    "Seçilen bir USB aygıtı bağlandığında otomasyonu başlatın.",
                    "Eşleştirilmiş seçili Bluetooth aygıtlarını bağlanıp ayrılırken izleyin.",
                    "Seçilen bir macOS ses çıkışı geçerli yönlendirme olduğu sürece oturumu etkin tutun.",
                    "Etkin çözümleyici yapılandırmasındaki seçili DNS sunucu adreslerini eşleştirin.",
                    "Tam IPv4 veya IPv6 adreslerini ve CIDR ağlarını eşleştirin.",
                    "Her yeni koşul türüne bağımsız bir oturum profili, ekran politikası ve en uzun süre atayın.",
                    "Yeni donanım ve ağ bağlamı kurallarını yeniden kullanılabilir iş akışı profillerine kaydedin.",
                    "İngilizce, Almanca, İspanyolca, Fransızca, Azerice ve Türkçe için eksiksiz arayüz desteği eklendi.",
                    "Disk görüntüsü artık büyük sürükle-kur simgeleri, yön oku ve Retina arka planıyla açılıyor.",
                ]),
                ("Gizlilik ve izinler",
                 "USB ve ses çıkışı algılama yerel macOS sistem API’lerini kullanır. Bluetooth kuralları yalnızca bağlı, eşleştirilmiş aygıtın kimliğine bakar ve standart macOS Bluetooth iznini gerektirir. Aygıt adları, DNS sunucu adresleri ve IP kuralları geçerli macOS kullanıcı hesabında kalır. Tanılama raporları yalnızca kural sayılarını ve etkin durumlarını içerir; yapılandırılmış aygıt adları, DNS sunucuları, IP kuralları ve etkinlik geçmişi dışarıda bırakılır."),
            ],
        },
    },
    {
        "version": "0.13.0", "date": (2026, 10, 1),
        "en": {
            "summary": "Extends automation to network context and external storage, and introduces reusable workflow profiles for complete rule configurations.",
            "sections": [
                ("Highlights", [
                    "Start automation on selected Wi-Fi networks.",
                    "Follow any active macOS VPN service.",
                    "Start a wake session when a selected external volume is mounted.",
                    "Use Drive Alive to refresh an owned marker on selected writable volumes at intervals from 5 to 60 minutes.",
                    "Save and restore complete automation configurations as named profiles.",
                    "Assign a session profile, display policy, and maximum duration independently to application, process, schedule, CPU, network, power, display, Wi-Fi, VPN, and drive conditions.",
                    "Review meaningful automation starts, stops, pauses, and condition changes in the local activity history.",
                    "Package the App Intents and App Shortcuts provider required for native Shortcuts discovery.",
                ]),
                ("Security and privacy",
                 "Wi-Fi names, selected volume names, and automation profile names remain in the current macOS user account. Drive Alive modifies only its signed ownership marker and removes it when disabled. Diagnostic reports exclude Wi-Fi, volume, application, process, and profile names."),
                ("Installer refresh — October 1, 2026",
                 "The signed and notarized disk image now opens with large application and Applications icons, a clear drag-to-install arrow, and a Retina background. The application remains version 0.13.0; the ZIP update package is unchanged. The disk-image SHA-256 checksum has been updated."),
            ],
        },
        "de": {
            "summary": "Erweitert die Automatisierung auf Netzwerkkontext und externe Speicher und führt wiederverwendbare Workflow-Profile für vollständige Regelkonfigurationen ein.",
            "sections": [
                ("Highlights", [
                    "Starte die Automatisierung in ausgewählten WLAN-Netzen.",
                    "Folge jedem aktiven macOS-VPN-Dienst.",
                    "Starte eine Wachhalte-Sitzung, wenn ein ausgewähltes externes Volume eingehängt wird.",
                    "Nutze Drive Alive, um in Intervallen von 5 bis 60 Minuten eine eigene Markierung auf ausgewählten beschreibbaren Volumes zu aktualisieren.",
                    "Speichere und stelle vollständige Automatisierungskonfigurationen als benannte Profile wieder her.",
                    "Weise Anwendungs-, Prozess-, Zeitplan-, CPU-, Netzwerk-, Strom-, Bildschirm-, WLAN-, VPN- und Laufwerksbedingungen jeweils unabhängig ein Sitzungsprofil, eine Bildschirmrichtlinie und eine Höchstdauer zu.",
                    "Prüfe relevante Starts, Stopps, Pausen und Bedingungsänderungen der Automatisierung im lokalen Aktivitätsverlauf.",
                    "Der für die native Erkennung in Kurzbefehle erforderliche App-Intents- und App-Shortcuts-Anbieter ist enthalten.",
                ]),
                ("Sicherheit und Datenschutz",
                 "WLAN-Namen, Namen ausgewählter Volumes und Namen von Automatisierungsprofilen bleiben im aktuellen macOS-Benutzerkonto. Drive Alive ändert nur die eigene signierte Eigentumsmarkierung und entfernt sie beim Deaktivieren. Diagnoseberichte schließen WLAN-, Volume-, Anwendungs-, Prozess- und Profilnamen aus."),
                ("Installer überarbeitet — 1. Oktober 2026",
                 "Das signierte und notarisierte Festplattenabbild öffnet sich jetzt mit großen Symbolen für die App und den Ordner „Programme“, einem klaren Pfeil zum Hineinziehen und einem Retina-Hintergrund. Die App bleibt Version 0.13.0; das ZIP-Updatepaket ist unverändert. Die SHA-256-Prüfsumme des Festplattenabbilds wurde aktualisiert."),
            ],
        },
        "tr": {
            "summary": "Otomasyonu ağ bağlamına ve harici depolamaya genişletir; eksiksiz kural yapılandırmaları için yeniden kullanılabilir iş akışı profilleri sunar.",
            "sections": [
                ("Öne çıkanlar", [
                    "Seçilen Wi-Fi ağlarında otomasyonu başlatın.",
                    "Etkin herhangi bir macOS VPN hizmetini izleyin.",
                    "Seçilen bir harici birim bağlandığında uyanık tutma oturumu başlatın.",
                    "Drive Alive ile seçili yazılabilir birimlerdeki kendi işaretçisini 5 ila 60 dakikalık aralıklarla yenileyin.",
                    "Eksiksiz otomasyon yapılandırmalarını adlandırılmış profiller olarak kaydedin ve geri yükleyin.",
                    "Uygulama, işlem, zamanlama, CPU, ağ, güç, ekran, Wi-Fi, VPN ve sürücü koşullarının her birine bağımsız bir oturum profili, ekran politikası ve en uzun süre atayın.",
                    "Anlamlı otomasyon başlangıçlarını, bitişlerini, duraklatmaları ve koşul değişikliklerini yerel etkinlik geçmişinde inceleyin.",
                    "Kısayollar’ın yerel olarak keşfedebilmesi için gereken App Intents ve App Shortcuts sağlayıcısı pakete eklendi.",
                ]),
                ("Güvenlik ve gizlilik",
                 "Wi-Fi adları, seçilen birim adları ve otomasyon profili adları geçerli macOS kullanıcı hesabında kalır. Drive Alive yalnızca kendi imzalı sahiplik işaretçisini değiştirir ve devre dışı bırakıldığında kaldırır. Tanılama raporları Wi-Fi, birim, uygulama, işlem ve profil adlarını dışarıda bırakır."),
                ("Yükleyici yenilendi — 1 Ekim 2026",
                 "İmzalı ve Apple tarafından onaylı disk görüntüsü artık büyük uygulama ve Programlar simgeleri, net bir sürükleyerek kurma oku ve Retina arka planıyla açılıyor. Uygulama 0.13.0 sürümünde kalır; ZIP güncelleme paketi değişmedi. Disk görüntüsünün SHA-256 sağlama toplamı güncellendi."),
            ],
        },
    },
    {
        "version": "0.12.0", "date": (2026, 10, 1),
        "en": {
            "summary": "Adds external control, process-aware automation, and bounded wake protection for long-running commands.",
            "sections": [
                ("Highlights", [
                    "Start, stop, toggle, and extend commands for Shortcuts through Open URL actions.",
                    "The `awakepilot://` URL scheme and bundled `awakepilotctl` command-line client.",
                    "Time-limited wake leases that release automatically when their owning process exits.",
                    "`awakepilotctl run -- <command>` for protecting any command throughout its lifetime.",
                    "Configurable terminal-process rules.",
                    "Any-condition and all-conditions automation matching.",
                    "Power-adapter and attached-display automation.",
                    "Critical thermal-pressure pauses and maximum automatic-session durations.",
                    "Optional remaining-time and automatic-session labels in the menu bar.",
                ]),
                ("Security and privacy",
                 "Wake leases are limited to 24 hours. A lease created by `awakepilotctl run` is released when its owning process exits, including orphan cleanup. Process rules compare executable names only; command text and output are not stored. Diagnostic reports exclude watched application and process names."),
            ],
        },
        "de": {
            "summary": "Ergänzt externe Steuerung, prozessbewusste Automatisierung und zeitlich begrenzten Wachhalteschutz für lang laufende Befehle.",
            "sections": [
                ("Highlights", [
                    "Start-, Stopp-, Umschalt- und Verlängerungsbefehle für Kurzbefehle über „URL öffnen“-Aktionen.",
                    "Das URL-Schema `awakepilot://` und der mitgelieferte Kommandozeilen-Client `awakepilotctl`.",
                    "Zeitlich begrenzte Wachhalte-Leases, die automatisch enden, wenn der zugehörige Prozess beendet wird.",
                    "`awakepilotctl run -- <Befehl>` schützt jeden Befehl über seine gesamte Laufzeit.",
                    "Konfigurierbare Regeln für Terminal-Prozesse.",
                    "Abgleich nach „eine Bedingung“ oder „alle Bedingungen“.",
                    "Automatisierung nach Netzteil und angeschlossenem Bildschirm.",
                    "Pausen bei kritischer thermischer Belastung und maximale Dauer automatischer Sitzungen.",
                    "Optionale Anzeige der Restzeit und automatischer Sitzungen in der Menüleiste.",
                ]),
                ("Sicherheit und Datenschutz",
                 "Wachhalte-Leases sind auf 24 Stunden begrenzt. Ein mit `awakepilotctl run` erzeugter Lease wird freigegeben, sobald der zugehörige Prozess endet, einschließlich der Bereinigung verwaister Leases. Prozessregeln vergleichen nur Namen ausführbarer Dateien; Befehlstext und Ausgabe werden nicht gespeichert. Diagnoseberichte schließen die Namen beobachteter Anwendungen und Prozesse aus."),
            ],
        },
        "tr": {
            "summary": "Dış denetim, işleme duyarlı otomasyon ve uzun süren komutlar için sınırlı uyanık tutma koruması ekler.",
            "sections": [
                ("Öne çıkanlar", [
                    "Kısayollar için Open URL eylemleriyle başlatma, durdurma, açıp kapatma ve süre uzatma komutları.",
                    "`awakepilot://` URL şeması ve pakete dahil `awakepilotctl` komut satırı istemcisi.",
                    "Sahibi olan işlem sona erdiğinde kendiliğinden bırakılan, süre sınırlı uyanık tutma kiraları.",
                    "Herhangi bir komutu yaşam süresi boyunca korumak için `awakepilotctl run -- <komut>`.",
                    "Yapılandırılabilir terminal işlemi kuralları.",
                    "Herhangi bir koşul ve tüm koşullar eşleştirme modları.",
                    "Güç adaptörü ve bağlı ekran otomasyonu.",
                    "Kritik ısıl baskıda duraklatma ve otomatik oturumlar için en uzun süre.",
                    "Menü çubuğunda isteğe bağlı kalan süre ve otomatik oturum etiketleri.",
                ]),
                ("Güvenlik ve gizlilik",
                 "Uyanık tutma kiraları 24 saatle sınırlıdır. `awakepilotctl run` ile oluşturulan kira, sahibi olan işlem sona erdiğinde (sahipsiz kalanların temizlenmesi dahil) bırakılır. İşlem kuralları yalnızca çalıştırılabilir dosya adlarını karşılaştırır; komut metni ve çıktısı saklanmaz. Tanılama raporları izlenen uygulama ve işlem adlarını dışarıda bırakır."),
            ],
        },
    },
    {
        "version": "0.11.0", "date": (2026, 10, 1),
        "en": {
            "summary": "Completes the first production distribution and support pipeline.",
            "sections": [
                ("Highlights", [
                    "Verified automatic update checks, downloads, and installation.",
                    "Apple-notarized ZIP and drag-to-install DMG packages.",
                    "About and Updates interface.",
                    "First-launch onboarding.",
                    "File-copy progress with percentage, throughput, and estimated time remaining.",
                    "Privacy-filtered diagnostic reports.",
                    "Continuous integration and the public product website.",
                    "Release and device-verification documentation.",
                ]),
                ("Security",
                 "Before installation, the updater verifies the downloaded package’s SHA-256 digest, bundle identity, Apple notarization status, and Developer ID signature."),
            ],
        },
        "de": {
            "summary": "Schließt die erste produktive Auslieferungs- und Support-Pipeline ab.",
            "sections": [
                ("Highlights", [
                    "Verifizierte automatische Update-Prüfungen, Downloads und Installation.",
                    "Von Apple notarisierte ZIP- und Drag-to-install-DMG-Pakete.",
                    "Oberfläche „Über und Updates“.",
                    "Einführung beim ersten Start.",
                    "Fortschritt beim Kopieren von Dateien mit Prozentwert, Durchsatz und geschätzter Restzeit.",
                    "Datenschutzgefilterte Diagnoseberichte.",
                    "Kontinuierliche Integration und die öffentliche Produkt-Website.",
                    "Dokumentation für Veröffentlichung und Geräteprüfung.",
                ]),
                ("Sicherheit",
                 "Vor der Installation prüft der Updater die SHA-256-Prüfsumme des heruntergeladenen Pakets, die Bundle-Identität, den Notarisierungsstatus bei Apple und die Developer-ID-Signatur."),
            ],
        },
        "tr": {
            "summary": "İlk üretim dağıtımı ve destek hattını tamamlar.",
            "sections": [
                ("Öne çıkanlar", [
                    "Doğrulanmış otomatik güncelleme denetimi, indirme ve kurulum.",
                    "Apple tarafından onaylı ZIP ve sürükleyerek kurulan DMG paketleri.",
                    "Hakkında ve Güncellemeler arayüzü.",
                    "İlk açılışta tanıtım.",
                    "Yüzde, aktarım hızı ve tahmini kalan süre gösteren dosya kopyalama ilerlemesi.",
                    "Gizlilik için süzülmüş tanılama raporları.",
                    "Sürekli entegrasyon ve herkese açık ürün web sitesi.",
                    "Sürüm ve aygıt doğrulama belgeleri.",
                ]),
                ("Güvenlik",
                 "Kurulumdan önce güncelleyici, indirilen paketin SHA-256 özetini, paket kimliğini, Apple onay durumunu ve Developer ID imzasını doğrular."),
            ],
        },
    },
]
