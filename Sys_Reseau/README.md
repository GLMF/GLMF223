# Are you safe?
par David Blaskow [Cyber chaos monkey à la solde de Data Essential]

---

Qu'est-ce qui vous garanti que vous êtes à l'abri ? Ces dernières années, nous avons vu passer pas mal de failles critiques telles que la CVE-2016-5195 [1] si joliment surnommée dirtycow ou la CVE-2017-5123 [2][3] qui utilise waitid(). Toutes les deux ont deux points communs : 1) de permettre de s'échapper d'un conteneur et devenir root de l'hôte 2) le hack se fait par le biais d'un appel système. Si ces failles sont aujourd'hui corrigées, comment allez-vous vous mettre à l'abri de la prochaine ? Êtes-vous en sécurité ?
