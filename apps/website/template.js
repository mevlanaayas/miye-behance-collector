/*
* Python script will create json file.
* Especially projects.
* add json field: (required job; updating js script at python side.)
* 	project_name
* 	cover_image
* 	project_publish_date
* 	description
* 	keywords
*   tags
* 	tools
* 	images
* 	view_count
* 	like_count
* after json created rearrange file according to the new fields.
*/
/*
This is empty on purpose! Your code to build the resume will go here.
 */
var project_json_variable = {
	'unique_project_array' : [

        {
            'project_title' : 'unique_project_name',
            'poster_image' : 'unique_cover_image',
            'publish_date' : 'unique_publish_date',
            'project_desc' : 'unique_project_desc',
            'keywords' : 'unique_keywords',
            'tags' : 'unique_tags',
            'tools' : 'unique_tools',
            'all_images_links' : 'unique_all_images_links',
            'view_count' : 'unique_view_count',
            'like_count' : 'unique_like_count'
        },
        {'next_project':'next'}
	]
};
var contactlinecolor = "purple";
var counter = 0;

var communication = {
	"email" : "ummiyemazlum@gmail.com",
	"location" : "Beşiktaş-İstanbul",
	"school": "Mimar Sinan University"
};

 var bio= {
	"name": "Ümmiye Mazlum",
	"role": "Graphic Designer",
	"hometown": "Trabzon",
	"language": "English",
	"image": "images/img.jpg",
	"welcomeMessage": "Welcome, here I am! All jobs are listed below thats were done by Ümmiye. If you want help, please dont hesitate to ask me!",
	"skills": {
		"C": 4,
		"Java": 3,
		"JavaScript": 4,
		"HTML/CSS": 4,
		"Python": 2,
		"Reliability": 5,
		"MicrosoftSQL": 3
	}
};

var projects = {
	"myprojects" : [
	{
		"title":"Binary Multiplication",
		"dates":"09/2015-10/2015",
		"describtion":"Multiplication of binary numbers by using data structure of linked list. Project extends some sorting algorithm and it was written with C programming language.",
		"skills" : "C Programming, Data Structures",
		"members" : 1,
		"files" : "none",
		"links" : "none",
		"type" : "Term Project",
		"img" : "none"

	}

	]
};

$("#creationsection").append(HTMLunderCreation);

function displayBio(argument) {
	var formattedforeign = HTMLbioForeign.replace("%data%", bio.language);
	var formattedHome = HTMLbioHome.replace("%data%", bio.hometown);
	var formattedName = HTMLheaderName.replace("%data%", bio.name);
	var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
	var formattedWelcome = HTMLwelcomeMsg.replace("%data%", bio.welcomeMessage);

	$("#nameid").append(formattedName);
	$("#role").append(formattedRole);
	$("#welcomeMssg").append(formattedWelcome);

	$("#welcomeMssg").append(HTMLBiosDropdown);
	$("#biotop").append(HTMLBios);
	$("#biotop").append(HTMLbioContent);

	$("#biocontent").append(formattedHome);
	$("#biocontent").append(formattedforeign);

	var formattedimg = HTMLbioPic.replace("%data%", bio.image);
	$("#pp").append(formattedimg);

	$("#skillsgeneric").append(HTMLskillsStart);
	for(skill in bio.skills){
		var formattedSkill = HTMLskills.replace("%data%",skill);
		$("#skillsdiv").append(formattedSkill);
		for(var i = 0; i<bio.skills[skill];i++){
			$("#skillsdiv").append('<i class="star yellow icon"></i>');
		}
	}
}

projects.display = function() {
	// body...

	for (project in projects.myprojects){
		//create a new div for projects
		$("#projects").append(HTMLprojectStart);


		var formattedprojectTitle = HTMLprojectTitle.replace("%data%", projects.myprojects[project].title);
		var formattedprojectDate = HTMLprojectDates.replace("%data%", projects.myprojects[project].dates);
		var formattedprojectDesc = HTMLprojectDescription.replace("%data%", projects.myprojects[project].describtion);
		var formattedprojectSkills = HTMLprojectSkills.replace("%data%", projects.myprojects[project].skills);

		if(projects.myprojects[project].members > 1){
			var formattedprojectMember = HTMLprojectMembers.replace("%data%", projects.myprojects[project].members);
		}else{
			var formattedprojectMember = HTMLprojectMember.replace("%data%", projects.myprojects[project].members);
		}
		var formattedprojectFiles = HTMLprojectFiles.replace("%data%", projects.myprojects[project].files);
		var formattedprojectLinks = HTMLprojectLinks.replace("%data%", projects.myprojects[project].links);
		var formattedprojectType = HTMLprojectType.replace("%data%", projects.myprojects[project].type);
		var formattedprojectImage = HTMLprojectImage.replace("%data%", projects.myprojects[project].img);


		if(counter > 1){
			$(".project-entry:last").append("<hr>");
		}

		$(".project-entry:last").append(formattedprojectTitle);

		$(".project-entry:last").append(formattedprojectDate);

		$(".project-entry:last").append(formattedprojectDesc);

		$(".project-entry:last").append(formattedprojectSkills);

		$(".project-entry:last").append(formattedprojectMember);

		$(".project-entry:last").append(formattedprojectFiles);

		$(".project-entry:last").append(formattedprojectLinks);

		$(".project-entry:last").append(formattedprojectType);

		$(".project-entry:last").append(formattedprojectImage);

		counter++;
	}

}
counter = 0;

communication.display = function () {
	// body...

	var formattedemail =  HTMLemail.replace("%color%", contactlinecolor);
	var formattedtwitter = HTMLtwitter.replace("%color%", contactlinecolor);
	var formattedgithub = HTMLgithub.replace("%color%", contactlinecolor);
	var formattedlocation = HTMLlocation.replace("%color%", contactlinecolor);

	var formattedemail =  formattedemail.replace("%data%", communication.email);
	var formattedtwitter = formattedtwitter.replace("%data%", communication.twitter);
	var formattedgithub = formattedgithub.replace("%data%", communication.github);
	var formattedlocation = formattedlocation.replace("%data%", communication.location);

	$("#connect").append(HTMLconnectStart);
	$(".connect-entry:last").append(formattedemail);
	$(".connect-entry:last").append(formattedtwitter);
	$(".connect-entry:last").append(formattedgithub);
	$(".connect-entry:last").append(formattedlocation);
}


counter = 0;
projects.display();
counter = 0;
displayBio();
counter = 0;
communication.display();
counter = 0;