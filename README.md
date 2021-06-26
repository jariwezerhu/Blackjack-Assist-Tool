# BlackJack
An algorithm that makes optimal decisions to advice players in real-time 
Blackjack Assist Tool
Jari Wezer										23/06/2021

Inleiding
In BlackJack.zip vindt u een assistentie-tool voor het spelen van Blackjack. 
Blackjack is een kaartspel dat (in casino’s) vaak om geld wordt gespeeld. Het doel van het spel is om de bank (dealer) te verslaan. Hierbij moet men proberen dichter bij de 21 punten te komen dan de bank. Als de speler boven de 21 punten uitkomt heeft hij verloren, ongeacht wat de bank heeft.
Het programma gaat uit van een aantal voorwaarden:
•	Dealer staat op soft 17;
•	Er wordt gespeeld met een (aantal) fysieke deck(s), wat wil zeggen dat kaarten niet teruggelegd worden nadat deze zijn gespeeld;
•	Er speelt minstens 1 speler en hoogstens 7;
•	Er is minstens 1 deck in spel en hoogstens 8;
•	Spelers kunnen (nog) niet verwijderd of toegevoegd worden nadat het spel begint.
Deze tool is niet bedoeld om gebruikt te worden bij het spelen om geld of met andere personen. Deze tool is puur educatief en een project om mijzelf mee uit te dagen.

Probleemomschrijving
Mijn vriend is verslaafd aan gokken. Hij verliest dan ook veel geld aan het casino. Om hem te helpen heb ik hem voorgesteld om een bot te maken, die het casino kan verslaan in Blackjack. Blackjack heeft goede kansen voor de speler, mits er strategie wordt toegepast. Verder zijn er bepaalde strategieën die kunnen worden toegepast om de speler zijn kansen nog erger te vergroten. Het casino wint dus niet altijd. Met een standaard strategie zijn de kansen 42.22% op winnen, 8.48% gelijkspel en 49.10% op verliezen. Het casino verslaat een speler dus. De functie van het programma is om als hulp-tool gebruikt te worden om een ‘edge’ tegen de dealer te krijgen.
Het programma moet minstens kaarten kunnen bijhouden. Op basis van deze kaarten moeten er aangepaste kansen weergeven worden. Het programma moet assistentie bieden aan de gebruiker. De kansen die worden weergegeven moeten accuraat zijn. Het programma moet snel genoeg meegaan om met een echt Blackjack potje mee te komen.
De bedoeling was om met deze bron dit algoritme aan te pakken https://inside.mines.edu/~mwakin/papers/mcbj.pdf (helaas was dit niet gelukt en heb ik mijn eigen oplossingen moeten bedenken).

Gebruik van het Programma
Extract de zipfile naar een map. Run om het programma te gebruiken ‘Main.py’. Let wel dat Python hiervoor geïnstalleerd dient te zijn.
Het programma zal vragen hoeveel decks er gebruikt worden. Holland Casino speelt bijvoorbeeld met 6 decks. De gebruiker kan hier zelf aangeven met hoeveel decks er gespeeld worden. Dit kan 1 deck zijn of 8 decks en alles ertussen. Vervolgens vraagt het programma hoeveel spelers er spelen. De gebruiker zal zelf moeten aangeven hoeveel spelers er zijn met keuze van 1 t/m 7. Vervolgens start het programma. Er zal geen Blackjack spel runnen op de computer, slechts een assistentie-tool. De gebruiker zal dus zelf moeten invoeren welke kaarten er getrokken worden per speler en door de dealer zelf. 
Het eerste wat de gebruiker te zien krijgt, zijn de kansen op Blackjack (21) met het huidige deck, een volledig deck en de kans verbetering t.o.v. een volledig deck. Hoe hoger deze score, hoe beter de kansen op Blackjack. Dit kan de speler gebruiken om een bet-grootte te kiezen. Vervolgens wordt per speler gevraagd welke kaarten zijn getrokken: de gebruiker dient deze zelf in te voeren. Als een ingevoerde kaart niet meer in het deck zit of ongeldig is, krijgt de gebruiker een error-code te zien. De gebruiker kan bijvoorbeeld “ace”, “Jack”, “q”, “K”, “3” o.i.d. invoeren en het programma zal deze kaart uit het deck halen en in de speler zijn hand zetten. Als de gebruiker voor alle spelers de kaarten heeft ingevoerd, worden er een aantal simulaties gerund. Dit kan een tijdje duren, afhangend van het aantal decks, het aantal spelers, het aantal simulaties en de uitkomsten. Het programma zal een suggestie doen of kansen weergeven, om de speler een idee te geven wat de beste zet is. De gebruiker kan een keuze maken uit “Hit”, “Stand”, “Double” en “Split. Momenteel werken “Double” en “Split” nog niet. De gebruiker dient deze nog niet gebruiken. Als alle spelers hun zetten en kaarten hebben, komt de dealer aan de beurt en geeft de gebruiker zijn kaarten aan (als de dealer geen kaart meer trekt omdat bijvoorbeeld elke speler Blackjack hit, kan de gebruiker 0 invoeren).
Tot slot herstart het programma om de volgende ronde te spelen. Het aantal kaarten reset niet, dus de Blackjack kansen zullen bijvoorbeeld geüpdatet zijn en de simulaties zullen andere uitkomsten hebben.

Problemen
De bedoeling was niet om dit een Monte Carlo gebaseerde oplossing te maken. Het doel was echter om perfecte kansen te berekenen. Dit wilde ik behalen door, op het moment dat alle kaarten gedeald zijn, over alle mogelijke kaartcombinaties heen te gaan, en hier de kansen van te berekenen. Het probleem echter is dat dit een NP-compleet probleem is. Wat dat wil zeggen is dat, hoewel dit mij gelukt was in de tweede week van het project, deze oplossing exponentieel was in tijdswaarde. In andere woorden: deze oplossing was veel te traag om in de werkelijkheid te gebruiken. Helaas ben ik de grootste hoeveelheid van mijn tijd kwijtgeraakt aan het proberen van een “Dynamic Programming” oplossing toe te passen. Nadat dit niet lukte, moest ik in de laatste paar dagen een Monte Carlo oplossing toepassen. Helaas is dit niet de manier waarop ik dit project wilde uitvoeren, en in de toekomst zou ik nogmaals proberen om een dynamische oplossing toe te passen. Het probleem om met Blackjack perfecte kansen uit te rekenen is ook wel een complexe versie van het subset sum probleem. Ik heb dus iets te veel hooi op mijn vork genomen. 
Daarnaast zijn de Monte Carlo uitkomsten niet optimaal gepresenteerd vanwege tijdsnood. Ik heb op de deadline van het project de laatste loodjes moeten leggen. In de toekomst zal ik dus beter mijn tijd moeten indelen en met name de haalbaarheid van mijn gekozen oplossing beter moeten inschatten.
 

 
