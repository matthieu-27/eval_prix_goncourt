/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP DATABASE IF EXISTS `goncourt_award`;
CREATE DATABASE IF NOT EXISTS `goncourt_award` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;
USE `goncourt_award`;

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `isbn` bigint(20) NOT NULL,
  `title` varchar(50) NOT NULL,
  `summary` text NOT NULL,
  `main_characters` varchar(200) NOT NULL,
  `release_date` date NOT NULL,
  `page_number` int(11) NOT NULL,
  `author_name` varchar(50) NOT NULL,
  `author_biography` text DEFAULT NULL,
  PRIMARY KEY (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `book` (`isbn`, `title`, `summary`, `main_characters`, `release_date`, `page_number`, `author_name`, `author_biography`) VALUES
	(9782021603439, 'Le bel obscur', 'Alors qu\'elle tente d\'élucider le destin d\'un ancêtre banni par sa famille une femme reprend l\'histoire de sa propre vie. Des années auparavant son mari son premier et grand amour lui a révélé être homosexuel. Du bouleversement que ce fut dans leur existence comme des péripéties de leur émancipation respective rien n\'est tu. Ce roman lumineux nous offre une leçon de courage de tolérance de curiosité aussi. Car jamais cette femme libre n\'aura cessé de se réinventer d\'affirmer la puissance de ses rêves contre les conventions sociales avec une fantaisie et une délicatesse infinies.\nCaroline Lamarche vit à Liège. Son œuvre témoigne d\'un éclectisme et d\'une hardiesse renouvelés de livre en livre. Elle a notamment obtenu le prix Rossel avec Le Jour du Chien (Les Éditions de Minuit) et le Goncourt de la nouvelle pour Nous sommes à la lisière (Gallimard). Elle signe avec Le Bel Obscur son retour au roman.', 'La romancière belge livre une réflexion saisissante d’intelligence sur le couple impossible qu’elle forma trente ans durant avec son mari homosexuel', '2021-12-01', 287, 'Caroline LAMARCHE', 'Caroline Lamarche vit à Liège. Son oeuvre témoigne d\'un éclectisme et d\'une hardiesse renouvelés de livre en livre. Elle a notamment obtenu le prix Rossel avec Le Jour du Chien (Les Éditions de Minuit) et le Goncourt de la nouvelle pour Nous sommes à la lisière (Gallimard). Elle signe avec Le Bel Obscur son retour au roman.'),
	(9782073101228, 'La collision', 'En 2012, en plein centre-ville de Lyon, une femme décède brutalement, percutée par un jeune garçon en moto cross qui fait du rodéo urbain à 80 km/h.\nDix ans plus tard, son fils, qui n\'a cessé d\'être hanté par le drame, est devenu journaliste. Il observe la façon dont ce genre de catastrophe est utilisé quotidiennement pour fracturer la société et dresser une partie de l\'opinion contre l\'autre. Il décide de se replonger dans la complexité de cet accident, et de se lancer sur les traces du motard pour comprendre d\'où il vient, quel a été son parcours et comment un tel événement a été rendu possible.\nEn décortiquant ce drame familial, Paul Gasnier révèle deux destins qui s\'écrivent en parallèle, dans la même ville, et qui s\'ignorent jusqu\'au jour où ils entrent violemment en collision. C\'est aussi l\'histoire de deux familles qui racontent chacune l\'évolution du pays. Un récit en forme d\'enquête littéraire qui explore la force de nos convictions quand le réel les met à mal, et les manquements collectifs qui créent l\'irrémédiable.', 'Paul Gasnier raconte le parcours de sa mère qui vient de créer un centre de Yoga et se rend à son travail à vélo. Mais aussi celui du jeune homme de dix-huit ans qui l’a tuée', '2021-12-01', 569, 'Paul GASNIER', 'Né en 1990, Paul Gasnier est journaliste. La collision est son premier récit.'),
	(9782073105455, 'Perpétuité', 'Guillaume Poix nous plonge dans l\'univers carcéral avec une intensité rare. À travers le récit de son incarcération pour un crime qu\'il n\'a pas commis, il explore les méandres de la justice, la solitude et la résilience humaine.\nLe roman suit le parcours de l\'auteur depuis son arrestation jusqu\'à son combat pour prouver son innocence. En décrivant avec précision la vie quotidienne en prison, les relations entre détenus et gardiens, ainsi que les défis psychologiques auxquels il est confronté, Poix offre une perspective unique sur un monde souvent méconnu.\nAvec une écriture poignante et introspective, Guillaume Poix nous invite à réfléchir sur la nature de la culpabilité et de la rédemption dans une société où la justice peut parfois être aveugle.', 'Un témoignage poignant sur la vie en prison et la quête de justice d\'\'un homme accusé à tort', '2021-12-01', 256, 'Guillaume POIX', NULL),
	(9782221267660, 'Le crépuscule des hommes', 'Nuremberg, 1945 : un procès fait l\'Histoire, eux la vivent. Un roman vrai, qui saisit les sursauts de l\'Histoire en marche.\nChacun connaît les images du procès de Nuremberg, où Göring et vingt autres nazis sont jugés à partir de novembre 1945. Mais que se passe-t-il hors de la salle d\'audience ?\nIls sont là : Joseph Kessel, Elsa Triolet, Martha Gellhorn ou encore John Dos Passos, venus assister à ces dix mois où doit oeuvrer la justice. Des dortoirs de l\'étrange château Faber-Castell, qui loge la presse internationale, aux box des accusés, tous partagent la frénésie des reportages, les frictions entre alliés occidentaux et soviétiques, l\'effroi que suscite le récit inédit des déportés.\nAvec autant de précision historique que de tension romanesque, Alfred de Montesquiou ressuscite des hommes et des femmes de l\'ombre, témoins du procès le plus retentissant du XXe siècle.', 'Un ouvrage passionnant et éclairant sur un événement exceptionnel dont on va bientôt commémorer les 80 ans.', '2021-12-01', 371, 'Alfred de MONTESQUIOU', NULL),
	(9782226498687, 'Un amour infini', 'À travers le récit de cette passion dévorante Ghislaine Dunant explore les méandres de l\'âme humaine et les complexités des relations amoureuses. Son écriture élégante et sensible nous plonge dans un univers où les émotions se mêlent aux souvenirs et aux rêves.\nLe roman aborde des thèmes universels tels que l\'amour, la perte, la rédemption et la quête de soi. Il nous invite à réfléchir sur la nature de l\'amour véritable et sur les sacrifices que l\'on est prêt à faire pour celui ou celle que l\'on aime.\nAvec une finesse psychologique remarquable Ghislaine Dunant nous offre un portrait poignant de personnages en quête de sens et d\'authenticité dans un monde souvent chaotique et incertain.', 'Une histoire d\'\'amour intense et bouleversante qui explore les profondeurs de l\'\'âme humaine', '2021-12-01', 384, 'Ghislaine DUNANT', ' Ghislaine Dunant a publié trois romans aux éditions Gallimard, dont son premier, très remarqué, L\'Impudeur (1989). Elle a reçu le prix Michel-Dentan (2008) pour Un effondrement et le prix Femina essai pour Charlotte Delbo. La vie retrouvée (2016), tous deux parus chez Grasset.'),
	(9782234097155, 'Tressaillir', 'Maria Pourchet nous offre un roman intime et bouleversant qui explore les thèmes de la maternité, de l\'identité et de la résilience. À travers le personnage de Claire, une femme confrontée à des défis personnels et familiaux, l\'auteur dépeint avec sensibilité les complexités des relations humaines et les luttes intérieures.\nLe récit suit Claire alors qu\'elle navigue entre ses responsabilités en tant que mère, ses aspirations personnelles et les attentes de la société. Maria Pourchet aborde avec finesse les émotions contradictoires qui accompagnent la maternité, tout en explorant les questions d\'autonomie et de liberté individuelle.\nAvec une prose élégante et une narration captivante, Tressaillir est un roman qui résonne profondément, offrant une réflexion sur la force intérieure nécessaire pour affronter les défis de la vie.', 'Un roman intime qui explore les complexités de la maternité et de l\'\'identité à travers le parcours d\'\'une femme en quête de sens', '2021-12-01', 312, 'Maria POURCHET', NULL),
	(9782234097278, 'Le nom des rois', '« Et d\'un seul coup, le monde qui servait de décor à tout cela s\'écroula. J\'en avais été un témoin distrait, mais le bruit qu\'il provoqua en s\'effondrant me fit lever la tête et ce que je vis alors n\'était plus qu\'un univers de violence et de mort. C\'est de celui-là que je suis devenu contemporain. J\'avais été, durant des années, dispensé d\'intérêt pour ce qui se passait autour de moi par ma passion des atlas, par les royautés anciennes et inutiles et par les terres lointaines et isolées, les berceaux de vieux empires oubliés.\nDésormais, l\'histoire se faisait sous mes yeux et je la trouvais moche, roturière et vulgaire. »\nDans ce récit de passage à l\'âge adulte porté par une écriture ample et élégante, Charif Majdalani raconte la disparition d\'un pays et explore ce qui subsiste de l\'enfance lorsqu\'elle capitule devant les fracas du monde.', 'Charif Majdalani raconte la disparition d\'\'un pays et explore ce qui subsiste de l\'\'enfance lorsqu\'elle capitule devant les fracas du monde', '2021-12-01', 394, 'Charif MAJDALANI', NULL),
	(9782260057307, 'L’adieu au visage', 'À la fin de l\'été 2019, David Deneufgermain apprend qu\'il est atteint d\'une maladie neurodégénérative rare et incurable : l\'atrophie multisystématisée. Il décide d\'écrire un journal intime pour témoigner de son combat contre la maladie et de son adieu progressif au monde qui l\'entoure.\nDans ce récit poignant, l\'auteur partage ses réflexions sur la vie, la mort, l\'amour et la résilience face à l\'adversité. Il évoque également les liens profonds qu\'il entretient avec sa famille et ses amis, ainsi que son attachement à la nature et à la beauté du monde qui l\'entoure.\nL\'adieu au visage est un témoignage bouleversant sur la condition humaine et la force de l\'esprit face à la maladie.', 'Un homme confronté à une maladie incurable décide de tenir un journal intime pour témoigner de son combat', '2021-12-01', 256, 'David DENEUFGERMAIN', 'David Deneufgermain est écrivain-médecin. Psychiatre, il a exercé en prison, en hôpital psychiatrique et soigne depuis onze ans les malades à la rue et dans son cabinet. L\'Adieu au visage est son premier roman du réel.'),
	(9782378562588, 'Tambora', 'Le 10 avril 1815 le mont Tambora sur l\'île de Sumbawa en Indonésie entre en éruption. C\'est la plus grande éruption volcanique jamais enregistrée dans l\'histoire de l\'humanité. Des dizaines de milliers de personnes périssent dans l\'immédiateté du cataclysme mais aussi dans les mois qui suivent à cause des famines et des épidémies provoquées par les cendres volcaniques qui ont envahi l\'atmosphère et obscurci le ciel mondial pendant plusieurs années.\nParmi les rares survivants de la catastrophe figure un jeune garçon de douze ans nommé Pakun qui va errer pendant des mois à travers l\'archipel indonésien avant d\'être recueilli par un missionnaire hollandais. C\'est à travers le regard de ce jeune garçon que Hélène Laurain nous fait revivre cette tragédie oubliée et nous plonge au cœur d\'un monde en pleine mutation entre traditions ancestrales et colonisation européenne.\nAvec une écriture poétique et immersive Hélène Laurain nous offre un roman historique captivant qui explore les thèmes de la résilience de la survie et de la quête d\'identité dans un contexte de bouleversements sociaux et environnementaux.', 'Un roman historique captivant qui explore les thèmes de la résilience et de la survie à travers le regard d\'\'un jeune garçon confronté à une catastrophe naturelle majeure', '2021-12-01', 352, 'Hélène LAURAIN', NULL),
	(9782707356741, 'La maison vide', 'En 1976, mon père a rouvert la maison qu\'il avait reçue de sa mère, restée fermée pendant vingt ans.\nÀ l\'intérieur : un piano, une commode au marbre ébréché, une Légion d\'honneur, des photographies sur lesquelles un visage a été découpé aux ciseaux.\nUne maison peuplée de récits, où se croisent deux guerres mondiales, la vie rurale de la première moitié du vingtième siècle, mais aussi Marguerite, ma grand-mère, sa mère Marie-Ernestine, la mère de celle-ci, et tous les hommes qui ont gravité autour d\'elles.\nToutes et tous ont marqué la maison et ont été progressivement effacés. J\'ai tenté de les ramener à la lumière pour comprendre ce qui a pu être leur histoire, et son ombre portée sur la nôtre.', 'Une famille confrontée à l’absence et au vide qui suit la perte d\'\'êtres chers', '2021-12-01', 774, 'Laurent MAUVIGNIER', NULL),
	(9782710015871, 'Où s’adosse le ciel', 'À la fin du XIXe siècle, Bilal Seck achève un pèlerinage à La Mecque et s\'apprête à rentrer à Saint-Louis du Sénégal. Une épidémie de choléra décime alors la région, mais Bilal en réchappe, sous le regard incrédule d\'un médecin français qui cherche à percer les secrets de son immunité. En pure perte. Déjà, Bilal est ailleurs, porté par une autre histoire, celle qu\'il ne cesse de psalmodier, un mythe immense, demeuré intact en lui, transmis par la grande chaîne de la parole qui le relie à ses ancêtres. Une odyssée qui fut celle du peuple égyptien, alors sous le joug des Ptolémées, conduite par Ounifer, grand prêtre d\'Osiris qui caressait le rêve de rendre leur liberté aux siens, les menant vers l\'ouest à travers les déserts, jusqu\'à une terre promise, un bel horizon, là où s\'adosse le ciel...\nCe chemin, Bilal l\'emprunte à son tour, vers son pays natal, en passant par Djenné, la cité rouge, où vint buter un temps le voyage d\'Ounifer et de son peuple.\nDe l\'Égypte ancienne au Sénégal, David Diop signe un roman magistral sur un homme parti à la reconquête de ses origines et des sources immémoriales de sa parole.', 'Un roman puissant qui explore les thèmes de l\'\'exil, de l\'\'identité et de la quête de soi à travers les voix croisées de plusieurs personnages', '2021-12-01', 320, 'David DIOP', 'Né en 1966, David Diop est l\'auteur de trois romans, dont deux publiés aux éditions du Seuil : Frère d\'âme (prix Goncourt des lycéens 2018, International Booker Prize 2021) et La Porte du voyage sans retour (finaliste du National Book Award 2023).'),
	(9782818061985, 'Kolkhoze', '🏆 Prix Médicis 2025 - Cette nuit-là, rassemblés tous les trois autour de notre mère, nous avons pour la dernière fois fait kolkhoze ', '«Kolkhoze» surnom donné aux nuits d\'\'enfance où Emmanuel Carrère et ses deux soeurs dormaient dans la chambre de leur mère en l\'\'absence du père', '2021-12-01', 667, 'Emmanuel CARRÈRE', 'Emmanuel Carrère est écrivain, scénariste et réalisateur. Il a publié une quinzaine de livres traduits dans le monde entier, dont L\'Adversaire, D\'autres vies que la mienne, Le Royaume, Yoga et V13.'),
	(9782823623376, 'Un frère', 'David Thomas nous plonge dans une histoire familiale poignante où les liens du sang sont mis à l\'épreuve par des secrets enfouis et des non-dits. À travers le personnage de Julien, un homme confronté à la disparition mystérieuse de son frère aîné, l\'auteur explore les thèmes de la fraternité, de la culpabilité et de la rédemption.\nLe roman suit Julien dans sa quête de vérité, à travers des flashbacks et des rencontres qui remettent en question ses certitudes. Avec un style narratif puissant et des descriptions évocatrices, David Thomas capture l\'essence des relations familiales et les émotions complexes qui en découlent.\nUn frère est un récit captivant qui invite à réfléchir sur la nature des liens familiaux et la manière dont ils façonnent notre identité.', 'Un roman bouleversant sur les liens fraternels et la quête de vérité au sein d\'\'une famille marquée par un secret', '2021-12-01', 208, 'David THOMAS', NULL),
	(9782848055701, 'Passagères de nuit', 'Dans ce nouveau roman comme arraché au chaos de son quotidien à Port-au-Prince Yanick Lahens rend un hommage d\'espoir et de résistance à la lignée des femmes dont elle est issue.\nLa première d\'entre elles Élizabeth Dubreuil naît vers 1820 à La Nouvelle-Orléans. Sa grand-mère arrivée d\'Haïti au début du siècle dans le sillage du maître de la plantation qui avait fini par l\'affranchir n\'a plus jamais voulu dépendre d\'un homme. Inspirée par ce puissant exemple la jeune Élisabeth se rebelle à son tour contre le désir prédateur d\'un ami de son père. Elle doit fuir la ville devenant à son tour une « passagère de nuit » sur un bateau à destination de Port-au-Prince. Ce qui adviendra d\'elle nous l\'apprendrons quand son existence croisera celle de Régina autre grande figure de ce roman des origines.\nNée pauvre parmi les pauvres dans un hameau du sud de l\'île d\'Haïti Régina elle aussi a forcé le destin : rien ne la déterminait à devenir la maîtresse d\'un des généraux arrivé en libérateur à Port-au-Prince en 1867. C\'est à « mon général mon amant mon homme » qu\'elle adresse le monologue amoureux dans lequel elle évoque sa trajectoire d\'émancipation : la cruauté mesquine des maîtres qu\'elle a fuis trouve son contrepoint dans les mains tendues par ces femmes qui lui ont appris à opposer aux coups du sort une ténacité silencieuse.\nCette ténacité silencieuse Élizabeth et Régina l\'ont reçue en partage de leurs lointaines ascendantes ces « passagères de nuit » des bateaux négriers dont Yanick Lahens évoque ici l\'effroyable réalité de même qu\'elle nous plonge – et ce n\'est pas la moindre qualité de ce très grand livre – dans les convulsions de l\'histoire haïtienne.\nLorsque les deux héroïnes se rencontreront dans une scène d\'une rare qualité d\'émotion nous lectrices et lecteurs comprendrons que l\'histoire ne s\'écrit pas seulement avec les vainqueurs mais dans la beauté des gestes des regards et des mystères tus qui à bas bruit montrent le chemin d\'une résistance forçant l\'admiration.', 'Raconte des femmes souveraines devenues guerrières dans le silence de l\'\'histoire d\'\'Haïti', '2021-12-01', 432, 'Yanick LAHENS', 'Lauréate du prix Femina 2014 pour Bain de lune, titulaire de la chaire des Mondes francophones au Collège de France en 2019, Yanick Lahens est née en 1953 en Haïti, où elle vit aujourd\'hui encore. Son oeuvre, traduite dans de nombreux pays, est publiée par Sabine Wespieser éditeur.'),
	(9931257824728, 'La nuit au cœur', '« De ces nuits et de ces vies, de ces femmes qui courent, de ces coeurs qui luttent, de ces instants qui sont si accablants qu\'ils ne rentrent pas dans la mesure du temps, il a fallu faire quelque chose. Il y a l\'impossibilité de la vérité entière à chaque page mais la quête désespérée d\'une justesse au plus près de la vie, de la nuit, du coeur, du corps, de l\'esprit.\nDe ces trois femmes, il a fallu commencer par la première, celle qui vient d\'avoir vingt-cinq ans quand elle court et qui est la seule à être encore en vie aujourd\'hui.\nCette femme, c\'est moi. »\nLa nuit au coeur entrelace trois histoires de femmes victimes de la violence de leur compagnon. Sur le fil entre force et humilité, Nathacha Appanah scrute l\'énigme insupportable du féminicide conjugal, quand la nuit noire prend la place de l\'amour.', 'trois femmes victimes de violence de leur compagnon', '2021-12-01', 476, 'Nathacha APPANAH', 'Nathacha Appanah est romancière. Ses romans ont été récompensés par plusieurs prix littéraires et traduits dans de nombreux pays. La nuit au coeur est son douzième livre.');

DROP TABLE IF EXISTS `editor`;
CREATE TABLE IF NOT EXISTS `editor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `editor_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `editor` (`id`, `editor_name`) VALUES
	(1, 'Robert Laffont'),
	(2, 'Minuit'),
	(3, 'Stock'),
	(4, 'Seuil'),
	(5, 'Sabine Wespieser'),
	(6, 'Gallimard'),
	(7, 'P.O.L'),
	(8, 'L’Olivier'),
	(9, 'Marchialy'),
	(10, 'Julliard'),
	(11, 'Albin Michel'),
	(12, 'Verticales'),
	(13, 'Verdier');

DROP TABLE IF EXISTS `editor_books`;
CREATE TABLE IF NOT EXISTS `editor_books` (
  `book_isbn` bigint(20) NOT NULL,
  `editor_id` int(11) NOT NULL,
  `editor_price` decimal(19,4) NOT NULL,
  PRIMARY KEY (`book_isbn`,`editor_id`),
  KEY `editor_id` (`editor_id`),
  CONSTRAINT `1` FOREIGN KEY (`book_isbn`) REFERENCES `book` (`isbn`),
  CONSTRAINT `2` FOREIGN KEY (`editor_id`) REFERENCES `editor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `editor_books` (`book_isbn`, `editor_id`, `editor_price`) VALUES
	(9782021603439, 4, 25.0000),
	(9782073101228, 6, 24.0000),
	(9782073105455, 12, 18.5000),
	(9782221267660, 1, 22.0000),
	(9782226498687, 11, 21.0000),
	(9782234097155, 3, 21.0000),
	(9782234097278, 3, 19.5000),
	(9782260057307, 9, 19.0000),
	(9782378562588, 13, 20.5000),
	(9782707356741, 2, 17.0000),
	(9782710015871, 10, 18.0000),
	(9782818061985, 7, 22.5000),
	(9782823623376, 8, 16.0000),
	(9782848055701, 5, 23.0000),
	(9931257824728, 6, 20.0000);

DROP TABLE IF EXISTS `jury`;
CREATE TABLE IF NOT EXISTS `jury` (
  `selection_id` int(11) NOT NULL,
  `personality_id` int(11) NOT NULL,
  PRIMARY KEY (`selection_id`,`personality_id`),
  KEY `personality_id` (`personality_id`),
  CONSTRAINT `1` FOREIGN KEY (`selection_id`) REFERENCES `selection` (`id`),
  CONSTRAINT `2` FOREIGN KEY (`personality_id`) REFERENCES `personality` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `jury` (`selection_id`, `personality_id`) VALUES
	(1, 1),
	(1, 2),
	(1, 3),
	(1, 4),
	(1, 5),
	(1, 6),
	(1, 7),
	(1, 8),
	(1, 9),
	(1, 10);

DROP TABLE IF EXISTS `personality`;
CREATE TABLE IF NOT EXISTS `personality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `is_president` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `personality` (`id`, `name`, `is_president`) VALUES
	(1, 'Didier Decoin', 0),
	(2, 'Françoise Chandernagor', 0),
	(3, 'Tahar Ben Jelloun', 0),
	(4, 'Paule Constant', 0),
	(5, 'Phillipe Claudel', 1),
	(6, 'Pierre Assouline', 0),
	(7, 'Eric-Emmanuel Schmitt', 0),
	(8, 'Camille Laurens', 0),
	(9, 'Pascal Bruckner', 0),
	(10, 'Christine Angot', 0);

DROP TABLE IF EXISTS `selection`;
CREATE TABLE IF NOT EXISTS `selection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `selection_number` int(11) NOT NULL,
  `vote_round` int(11) NOT NULL,
  `selection_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `selection` (`id`, `selection_number`, `vote_round`, `selection_date`) VALUES
	(1, 1, 1, '2025-09-01');

DROP TABLE IF EXISTS `selection_books`;
CREATE TABLE IF NOT EXISTS `selection_books` (
  `book_isbn` bigint(20) NOT NULL,
  `selection_id` int(11) NOT NULL,
  `number_of_votes` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`book_isbn`,`selection_id`),
  KEY `selection_id` (`selection_id`),
  CONSTRAINT `1` FOREIGN KEY (`book_isbn`) REFERENCES `book` (`isbn`),
  CONSTRAINT `2` FOREIGN KEY (`selection_id`) REFERENCES `selection` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `selection_books` (`book_isbn`, `selection_id`, `number_of_votes`) VALUES
	(9782021603439, 1, 0),
	(9782073101228, 1, 0),
	(9782073105455, 1, 0),
	(9782221267660, 1, 0),
	(9782226498687, 1, 0),
	(9782234097155, 1, 0),
	(9782234097278, 1, 0),
	(9782260057307, 1, 0),
	(9782378562588, 1, 0),
	(9782707356741, 1, 0),
	(9782710015871, 1, 0),
	(9782818061985, 1, 0),
	(9782823623376, 1, 0),
	(9782848055701, 1, 0),
	(9931257824728, 1, 0);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
