input = getDirectory("Input Directory");
output = input; // Output images to the same directory as input (prevents second dialogue box, otherwise getDirectory("Output Directory"))
Dialog.create("File Type");
Dialog.addString("File Suffix: ", ".JPG", 5); // Select another file format if desired
suffix = Dialog.getString();


Dialog.create("test");
Dialog.addString("Please enter the project name", "empty");
Dialog.show();
expcode = Dialog.getString();

print("project name recorded, will be used for creating the final csv file.");



processFolder(input);

// Scan folders/subfolders/files to locate files with the correct suffix

function processFolder(input) {
	list = getFileList(input);
	for (i = 0; i < list.length; i++) {
		if(File.isDirectory(input + list[i]))
			processFolder("" + input + list[i]);
		if(endsWith(list[i], suffix))
			processFile(input, output, list[i]);
	}
}




// LOOP

function processFile(input, output, file) {


open(file);
filename = File.name;


//setTool("line");                                       
//beep();                                              
//waitForUser("Please select a scale unit (1mm)! and press OK.");
//run("Set Scale...", "known=1 pixel=1 unit=mm");
//print("Scale defined , 1mm.");


run("Set Scale...", "distance=20 known=1 unit=mm");
j = nResults;

setTool("line");
waitForUser("Select standard length and press OK.");
List.setMeasurements;
stdleng = List.getValue("Length");
setResult("Standard_Length", j, stdleng);
print("standard length added.");

//setTool("line");
//waitForUser("Select total length and press OK.");
//List.setMeasurements;
//totleng = List.getValue("Length");
//setResult("Total_Length", j, totleng);
//print("total length added.");

setResult("Image_ID", j, filename);
print("filename added");
close();


}

updateResults()
saveAs("Results", input + expcode + "_length_saury.csv");

print("Table saved in same directory as pictures.");

print("Task complete.");




