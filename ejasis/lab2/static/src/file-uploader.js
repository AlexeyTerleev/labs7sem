async function handleLr2Results(file) {
  const lr2_results_list = document.getElementById("lr2-result-list");

  try {
    const response = await fetch(`/access_file_content?file_name=${file.name}`);
    const data = await response.json();

    const fwResponce = await fetch(`/frequency?current_file=${data.raw_text}`);
    const fwData = await fwResponce.json();

    const abcResponce = await fetch(`/alphabetical?current_file=${data.raw_text}`);
    const abc_data = await abcResponce.json();

    const neuralResponce = await fetch(`/neural?current_file=${data.raw_text}`);
    const neuralData = await neuralResponce.json();

    const newItem = document.createElement("li");
    newItem.classList.add("lr2-result-list-items");
    const itemData = [
      `File name: ${file.name}`,
      `Alphabet method: ${abc_data.language};`,
      `Frequency words methods: ${fwData.language};`,
      `Neural method: ${neuralData.language} ${file.name}`,
    ];

    itemData.forEach(item => {
      const itemDataEl = document.createElement("div");
      itemDataEl.textContent = item;
      newItem.appendChild(itemDataEl)
    })

    const linkItem = document.createElement("a");
    linkItem.href = `http://${window.location.host}/access_file_content?file_name=${file.name}` 
    linkItem.target = "_blank";

    linkItem.appendChild(newItem);
    lr2_results_list.appendChild(linkItem);
  } catch (error) {
    console.error("Error fetching file content:", error);
  }
}

// Function to create HTML for each file item
const createFileItemHTML = (file, uniqueIdentifier) => {
  // Extracting file name, size, and extension
  const { name, size } = file;
  const extension = name.split(".").pop();
  const formattedFileSize =
    size >= 1024 * 1024
      ? `${(size / (1024 * 1024)).toFixed(2)} MB`
      : `${(size / 1024).toFixed(2)} KB`;

  // Generating HTML for file item
  return `
  <li class="file-item" id="file-item-${uniqueIdentifier}">
    <div class="file-extension">${extension}</div>
      <div class="file-content-wrapper">
        <div class="file-content">
          <div class="file-details">
            <h5 class="file-name">${name}</h5>
            <div class="file-info">
              <small class="file-size">0 MB / ${formattedFileSize}</small>
              <small class="file-divider">•</small>
              <small class="file-status">Uploading...</small>
            </div> 
          </div>
          <button class="cancel-button">
            <i class="bx bx-x"></i>
          </button>
        </div>
      <div class="file-progress-bar">
          <div class="file-progress"></div>
      </div>
    </div>
  </li>`;
};


const handleFileUploading = (file, uniqueIdentifier) => {
  const xhr = new XMLHttpRequest();
  const formData = new FormData();
  formData.append("file", file);

  xhr.upload.addEventListener("progress", (e) => {
    const fileProgress = document.querySelector(`#file-item-${uniqueIdentifier} .file-progress`);
    const fileSize = document.querySelector(`#file-item-${uniqueIdentifier} .file-size`);

    const formattedFileSize =
      file.size >= 1024 * 1024
        ? `${(e.loaded / (1024 * 1024)).toFixed(2)} MB / ${(e.total / (1024 * 1024)).toFixed(2)} MB`
        : `${(e.loaded / 1024).toFixed(2)} KB / ${(e.total / 1024).toFixed(2)} KB`;

    const progress = Math.round((e.loaded / e.total) * 100);
    fileProgress.style.width = `${progress}%`;
    fileSize.innerText = formattedFileSize;
  });

  xhr.open("POST", "http://localhost:8000/upload_file", true);
  xhr.send(formData);
  return xhr;
};


const handleSelectedFiles = ([...files]) => {
  const fileList = document.querySelector(".file-list");

  let completedFiles = 0;
  if (files.length === 0) 
    return;

  files.forEach((file, index) => {
    const fileItemHTML = createFileItemHTML(file, index);
    fileList.insertAdjacentHTML("afterbegin", fileItemHTML);
    const currentFileItem = document.querySelector(`#file-item-${index}`);
    const cancelFileUploadButton = currentFileItem.querySelector(".cancel-button");

    const xhr = handleFileUploading(file, index);
    
    handleLr2Results(file);

    const updateFileStatus = (status, color) => {
      currentFileItem.querySelector(".file-status").innerText = status;
      currentFileItem.querySelector(".file-status").style.color = color;
    };

    xhr.addEventListener("readystatechange", () => {
      // Handling completion of file upload
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        completedFiles++;
        cancelFileUploadButton.remove();
        updateFileStatus("Completed", "#00B125");
      }
    });

    // Handling cancellation of file upload
    cancelFileUploadButton.addEventListener("click", () => {
      xhr.abort(); // Cancel file upload
      updateFileStatus("Cancelled", "#E3413F");
      cancelFileUploadButton.remove();
    });

    // Show Alert if there is any error occured during file uploading
    xhr.addEventListener("error", () => {
      updateFileStatus("Error", "#E3413F");
      alert("An error occurred during the file upload!");
    });
  });

};


document.addEventListener("DOMContentLoaded", () => {

  const fileBrowseButton = document.querySelector(".file-browse-button");
  const fileBrowseInput = document.querySelector(".file-browse-input");
  const fileUploadBox = document.querySelector(".file-upload-box");

  fileUploadBox.addEventListener("drop", (e) => {
    e.preventDefault();
    handleSelectedFiles(e.dataTransfer.files);
    fileUploadBox.classList.remove("active");
    fileUploadBox.querySelector(".file-instruction").innerText = "Drag files here or";
  });
  
  fileUploadBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    fileUploadBox.classList.add("active");
    fileUploadBox.querySelector(".file-instruction").innerText = "Release to upload or";
  });
  
  fileUploadBox.addEventListener("dragleave", (e) => {
    e.preventDefault();
    fileUploadBox.classList.remove("active");
    fileUploadBox.querySelector(".file-instruction").innerText = "Drag files here or";
  });
  
  if (!fileBrowseInput || !fileBrowseButton) {
    console.error("fileBrowseInput or fileBrowseButton element not found");
    return;
  }

  fileBrowseInput.addEventListener("change", (e) => {
    if (e.target.files) {
      handleSelectedFiles(e.target.files); 
    }
  });

  fileBrowseButton.addEventListener("click", () => fileBrowseInput.click());
});
