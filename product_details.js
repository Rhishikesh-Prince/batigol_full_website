document.addEventListener("DOMContentLoaded", () => {

	const price = 500;

	const quantityInput = document.getElementById("quantity");
	const totalPrice = document.getElementById("totalPrice");

	const bulkSection = document.getElementById("bulkSection");
	const customSection = document.getElementById("customSection");

	const radios = document.querySelectorAll("input[name='orderType']");
	const container = document.getElementById("playersContainer");

	/* ---------- IMAGE SWITCH ---------- */

	const mainImage = document.getElementById("mainImage");
	const thumbs = document.querySelectorAll(".thumb");

	thumbs.forEach(thumb => {
		thumb.addEventListener("click", () => {

			mainImage.src = thumb.src;

			thumbs.forEach(t => t.classList.remove("active"));
			thumb.classList.add("active");

		});
	});

	/* ---------- PLAYER ADD ---------- */

	window.addPlayer = function(){

		const row = document.createElement("div");
		row.classList.add("player-row");

		row.innerHTML = `
			<input type="text" placeholder="Name">
			<input type="text" placeholder="Number">
			<select>
				<option>S</option>
				<option>M</option>
				<option>L</option>
				<option>XL</option>
			</select>
		`;

		container.appendChild(row);

		updateTotalCustom();
	}

	/* ---------- BULK TOTAL ---------- */

	function updateTotalBulk(){

		let qty = parseInt(quantityInput.value);

		if(qty < 10){
			qty = 10;
			quantityInput.value = 10;
		}

		totalPrice.innerText = qty * price;
	}

	/* ---------- CUSTOM TOTAL ---------- */

	function updateTotalCustom(){

		let count = container.children.length;

		if(count === 0){
			totalPrice.innerText = 0;
		}else{
			totalPrice.innerText = count * price;
		}
	}

	/* ---------- SWITCH MODE ---------- */

	radios.forEach(radio => {

		radio.addEventListener("change", () => {

			if(radio.value === "bulk"){

				bulkSection.style.display = "block";
				customSection.style.display = "none";

				updateTotalBulk();

			}else{

				bulkSection.style.display = "none";
				customSection.style.display = "block";

				totalPrice.innerText = 0;

			}

		});

	});

	/* ---------- EVENTS ---------- */

	quantityInput.addEventListener("input", updateTotalBulk);

	/* ---------- INITIAL ---------- */

	updateTotalBulk();

});