
import axios from 'axios';
import JobDetails from '../../src/components/job/JobDetails';
import Layout from '../../src/components/layout/Layout';
import NotFound from '../../src/components/layout/NotFound';


export default function JobDetailsPage({job, candidates, error}) {

    if(error) {
        return <NotFound />
    }
    console.log(error)
  return (
    <Layout title={job.title}>
        <JobDetails job={job} candidates={candidates}/>
    </Layout>
  );
}


export async function getServerSideProps({params}) {
    try{
        const response = await axios.get(`${process.env.API_URL}/api/jobs/${params.id}`)
        const job = response.data.job;
        const candidates = response.data.candidates;
    
    
      return {
        props: {
          job,
          candidates
        }
      }
    } catch(err){
        return {
            props: {
                error: err.response.data.detail,
            }
        }
    }
    
}