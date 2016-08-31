<div class="row">

	<div class="col-md-12">
	
		<h2 style="text-align: center">{{time}} : /index reached!</h2>
		<br>
		<p style="text-align: center">{{msg}}</p>
	
		<form action="/index" method="post" enctype="multipart/form-data">
			<input style="width: 100%; margin: auto; text-align: center" type="text" name="token" value="{{token}}">
			<button type="submit" style="display: block; margin: auto" class="btn btn-default btn-lg">
				Submit
			</button>
		</form>

		<form action="/index" method="get">
			<button type="submit" style="display: block; margin: auto" class="btn btn-default btn-lg">
				Refresh
			</button>
		</form>

		<ol>
		% for r in records:
			<li>{{r}}</li>
		% end
		</ol>
	
	</div>

</div>