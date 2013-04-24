"""netcdf example that clones an ncfile
"""

from netCDF4 import Dataset
import glob

#
# assume we've got a single file that's
# uniquely identfied by this regexp
#
ncfile_in=glob.glob("toga*nc")[0]
run_num=1
ncfile_out="run_{0:d}_{1:s}".format(run_num,ncfile_in)
infile = Dataset(ncfile_in, 'r')
outfile = Dataset(ncfile_out,mode='w',format='NETCDF3_CLASSIC')
#first transfer the dimensions

print infile.variables.keys()
new_temp=infile.variables['T']
new_temp=new_temp[...]


for (name,value) in infile.dimensions.items():
    outfile.createDimension(name,len(value))

#next tranfer the global attributes

for globalatt in infile.ncattrs():
    print "copying global attribute: ",globalatt
    outfile.setncattr(globalatt,infile.getncattr(globalatt))

#transfer each variable and its attributes

for (inname,invalue) in infile.variables.items():
    print "copying variable: ",inname
    #create the variable
    outvar = outfile.createVariable(inname,invalue.dtype,invalue.dimensions)
    #transfer the attributes
    for varattr in invalue.ncattrs():
        outvar.setncattr(varattr,invalue.getncattr(varattr))
    ## #finally, copy the data
    outvar[...]=invalue[...]

infile.close()

transformed_vars=['press','temp','theta']

for the_var in tranformed_vars:
    the_array=oufile.variables[the_var]
    the_array[...]=newvars[the_var][...]
    print type(the_array)
    
    

outfile.close()
