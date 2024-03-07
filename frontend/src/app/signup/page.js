import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle,
} from '@/components/ui/card'
import RegisterForm from '@/components/register-form'
import { Button } from '@/components/ui/button'
import Link from 'next/link'

export default function SignUp() {
	return (
		<section className='flex-1 flex'>
			<div className='container mx-auto mt-4 flex items-center justify-center'>
				<Card className='w-[350px]'>
					<CardHeader>
						<CardTitle>Create an account</CardTitle>
						<CardDescription>
							Enter your email below to create your account
						</CardDescription>
					</CardHeader>
					<CardContent className='grid gap-4'>
						<RegisterForm />
						{/* <div className='relative'>
							<div className='absolute inset-0 flex items-center'>
								<span className='w-full border-t'></span>
							</div>
							<div className='relative flex justify-center text-xs uppercase'>
								<span className='bg-background px-2 text-muted-foreground'>
									Or continue with
								</span>
							</div>
						</div> */}
					</CardContent>
					<CardFooter className='flex justify-center'>
						<Button asChild variant='link'>
							<Link href={'/login'}>Already have an account?</Link>
						</Button>
					</CardFooter>
					{/* TODO: Autenticar con Google y GitHub */}
					{/* <CardFooter className='grid grid-cols-2 gap-6'>
						<Button asChild variant='outline'>
							<Link href={'#'}>
								<GitHubLogoIcon className='mr-2 h-4 w-4' /> GitHub
							</Link>
						</Button>
						<Button asChild variant='outline'>
							<Link href={'#'}>
								<GoogleIcon className='mr-2 h-4 w-4 fill-black dark:fill-white' />
								Google
							</Link>
						</Button>
					</CardFooter> */}
				</Card>
			</div>
		</section>
	)
}
