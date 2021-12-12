xml format is:

```xml
<?xml version="1.0" ?>
<coverage version="" timestamp="" lines-valid="" lines-covered="" line-rate="" branches-covered="" branches-valid="" branch-rate="" complexity="">
	<sources>
		<source></source>
	</sources>
	<packages>
		<package name="" line-rate="" branch-rate="" complexity="">
			<classes>
				<class name="" filename="" complexity="" line-rate="" branch-rate="">
					<methods/>
					<lines>
						<line number="" hits=""/>
					</lines>
				</class>
			</classes>
		</package>
	</packages>
</coverage>
```

validate with: 
```shell
npx openapi-generator-cli validate cover-rest_api_spec_v1.yaml
```

generate with: 
```shell
npx openapi-generator-cli generate cover-rest_api_spec_v1.yaml
```