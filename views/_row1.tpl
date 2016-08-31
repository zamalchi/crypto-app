<div class="row">

	<div class="col-md-12">
	
		<h2 style="text-align: center">{{time}} : /index reached!</h2>
		<br>
		<p style="text-align: center">{{msg}}</p>
	
		<form action="/index" method="post" enctype="multipart/form-data" style="display: inline">
			<input style="width: 100%; margin: auto; text-align: center" type="text" name="token" value="{{token}}">
			<button type="submit" style="display: inline" class="btn btn-default btn-lg">
				Submit
			</button>
		</form>

		<form action="/index" method="get" style="display: inline">
			<button type="submit" style="display: inline" class="btn btn-default btn-lg">
				Refresh
			</button>
		</form>

		<a href="http://127.0.0.1:8080/hours" target="_blank" style="display: inline" class="btn btn-default btn-info btn-lg">Hours</a>

		<br><br>

		<ol>
		% for r in records:
			<li>{{r}}</li>
		% end
		</ol>
	
	</div>

</div>